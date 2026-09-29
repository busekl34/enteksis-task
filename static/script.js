const form = document.getElementById("requestForm");
const submitButton = document.getElementById("submitButton");
const formStatus = document.getElementById("formStatus");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const service = document.getElementById("service").value;
    const description = document.getElementById("description").value.trim();

    formStatus.className = "status loading";
    formStatus.textContent = "Talebiniz gönderiliyor...";
    
    submitButton.disabled = true;
    submitButton.textContent = "Gönderiliyor...";

    try {
        const response = await fetch("/api/requests", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name,
                email,
                service,
                description
            })
        });

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error(result.message || "Talep gönderilemedi.");
        }

        formStatus.className = "status success";
        formStatus.textContent = result.message;

        form.reset();

    } catch (error) {
        formStatus.className = "status error";
        formStatus.textContent = error.message || "Bir hata oluştu.";

    } finally {
        submitButton.disabled = false;
        submitButton.textContent = "Talep Gönder";
    }
});