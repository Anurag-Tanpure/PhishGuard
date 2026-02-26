chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "check_url_api") {
        
        fetch("http://localhost:8080/api/check-url", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: request.url })
        })
        .then(res => res.json())
        .then(data => {
            // Data should be { "message": "...", "confidence": 85 }
            sendResponse({ status: "success", data: data });
        })
        .catch(err => {
            console.error("Fetch error:", err);
            sendResponse({ status: "error" });
        });

        return true; // Keep channel open
    }
});