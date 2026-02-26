let clickTimer = null;

document.addEventListener("click", function (event) {
    let target = event.target.closest("A");
    if (!target) return;

    // If a double-click is already in progress, stop the single click from opening the link
    if (clickTimer !== null) {
        event.preventDefault();
        return;
    }

    // Standard single click behavior (opens link normally)
});

document.addEventListener("dblclick", function (event) {
    let target = event.target.closest("A");
    if (!target) return;

    // 1. STOP the link from opening
    event.preventDefault();
    event.stopPropagation();
    
    // Clear any pending single-click timers
    clickTimer = true; 
    setTimeout(() => { clickTimer = null; }, 500);

    const clickedUrl = target.href;
    console.log("🛠 Double-click detected. Analyzing:", clickedUrl);

    // 2. Visual Loading Feedback
    const statusMsg = document.createElement('div');
    statusMsg.innerHTML = "🔍 <b>Scanning Link...</b> Please wait.";
    statusMsg.style = "position:fixed; top:20px; left:50%; transform:translateX(-50%); background:#222; color:#fff; padding:15px 25px; border-radius:30px; z-index:1000000; font-family:sans-serif; border:2px solid #444;";
    document.body.appendChild(statusMsg);

    // 3. Send to Background Script
    chrome.runtime.sendMessage({ action: "check_url_api", url: clickedUrl }, (response) => {
        statusMsg.remove(); // Remove loading message

        if (response && response.status === "success") {
            const confidence = parseFloat(response.data.confidence);
            
            // 4. Logic: Confidence >= 80 means Phishing
            if (confidence >= 80) {
                alert(`🚨 PHISHING DETECTED! 🚨\n\nWarning: This URL is dangerous.\nConfidence: ${confidence}%\n\nAccess to this site has been blocked for your safety.`);
            } else {
                if (confirm(`✅ URL Looks Safe.\nConfidence: ${confidence}%\n\nDo you want to visit this page?`)) {
                    window.location.href = clickedUrl;
                }
            }
        } else {
            alert("❌ Detection Error: Could not connect to Python server.");
        }
    });
}, true);