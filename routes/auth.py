from flask import Blueprint, render_template, request, redirect, url_for, session


def auth_bp():
    bp = Blueprint("auth", __name__, url_prefix="/auth")

    @bp.get("/login")
    def login_form():
        return render_template("login.html", error=None, form={})

    @bp.post("/login")
    def login_submit():
        form = request.form.to_dict()
        username = (form.get("username") or "").strip()
        password = form.get("password") or ""
        # Very simple demo credentials; replace with real user store
        if username == "admin" and password == "admin":
            session["user"] = {"username": username}
            next_url = request.args.get("next") or url_for("index")
            return redirect(next_url)
        return render_template("login.html", error="Invalid credentials", form=form), 401

    @bp.get("/logout")
    def logout():
        session.pop("user", None)
        return redirect(url_for("auth.login_form"))

    return bp
