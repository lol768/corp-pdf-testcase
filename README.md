# crbug952834
MRE for Chrome bug [952834](https://bugs.chromium.org/p/chromium/issues/detail?id=952834)

To run, use `go run app.go` and visit http://localhost:8080/

Click on either link and try to save the resource. Right click from the main page also reproduces the problem.

Version 73.0.3683.103 (Official Build) (64-bit)

# crbug1074261

MRE for Chrome bug [1074261](https://bugs.chromium.org/p/chromium/issues/detail?id=1074261)

To run, use `go run app.go` and visit http://localhost:8080/main.pdf

Observe that only the first page is rendered and the other pages appear as discs which do not load.

Version 81.0.4044.122 (Official Build) snap (64-bit)

# bugzil.la/1638323

MRE for Firefox bug [1638323](https://bugzilla.mozilla.org/show_bug.cgi?id=1638323)

To run, use `go run app.go` and visit http://localhost:8080/main.pdf

Open the PDF and try to save the resource by pressing Ctrl+S or using file -> save page as.

Note that the magpie downloads correctly in Firefox.
