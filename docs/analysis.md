# Analysis
- Issues found: coupling (routes did logic + data), globals, duplication, missing tests.
- Initial metrics: (run `radon cc -s -a .`, `radon mi .`, `radon raw .` and paste here)
- Risks: in-memory data cleared on restart; behavior should stay same unless noted.