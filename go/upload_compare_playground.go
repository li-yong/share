// This program shares the text from standard input on the Go Playground and then retrieves the shared code.
// It compares the original input with the retrieved code and reports whether they match or not.

// Features:
// 1. Reads text from standard input.
// 2. Sends the text to the Go Playground share endpoint using an HTTP POST request.
// 3. Retrieves the share ID from the response and constructs a shareable URL.
// 4. Fetches the code content from the constructed URL using an HTTP GET request.
// 5. Compares the original input with the retrieved code.
// 
// Example:
// >go build upload_compare_playground.go
// 
// >cat hello.go | 1.exe
// Shareable URL: https://play.golang.org/p/HmnNoBf0p1z
// Code:
// package main
// 
// import (
//         "fmt"
// )
// 
// func main() {
//         fmt.Println("Hello, playground")
// }
// 
// Retrieved code matches the original input!
// 
// Ref: https://stackoverflow.com/questions/50690446/how-to-retrieve-golang-code-from-shared-play-golang-org-url



package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
)

func main() {
    // Read the program text from stdin
    data, err := ioutil.ReadAll(os.Stdin)
    if err != nil {
        fmt.Println("Error reading from stdin:", err)
        return
    }

    // Create an HTTP POST request to the playground share endpoint
    req, err := http.NewRequest("POST", "https://play.golang.org/share", bytes.NewBuffer(data))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }
    req.Header.Set("Content-Type", "text/plain; charset=utf-8")

    // Send the request
    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    // Read the response body (which contains the share ID)
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response:", err)
        return
    }

    // Construct the full HTTP URL with the share ID
    shareURL := "https://play.golang.org/p/" + string(body)
    fmt.Println("Shareable URL:", shareURL)

	
	//------------------------

    // Construct the URL to fetch the code
    codeURL := shareURL + ".go"

    // Fetch the code content
    resp, err = http.Get(codeURL)
    if err != nil {
        fmt.Println("Error fetching code:", err)
        return
    }
    defer resp.Body.Close()

    code, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading code content:", err)
        return
    }

    // Print the retrieved code
    fmt.Println("Code:")
    fmt.Println(string(code))	
	
	//----------------------------
	    // Compare the original input (data) with the retrieved code
    if bytes.Equal(data, code) {
        fmt.Println("Retrieved code matches the original input!")
    } else {
        fmt.Println("Retrieved code does not match the original input.")
    }
}