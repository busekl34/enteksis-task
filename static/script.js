const form = document.getElementById("requestForm");
const submitButton = document.getElementById("submitButton");
const formStatus = document.getElementById("formStatus");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    formStatus.className = "form-status loading";
    formStatus.textContent = "Talebiniz gönderiliyor...";

    submitButton.disabled = true;
    submitButton.textContent = "Gönderiliyor...";

    const formData = {
        name: document.getElementById("name").value.trim(),
        email: document.getElementById("email").value.trim(),
        service: document.getElementById("service").value,
        description: document.getElementById("description").value.trim()
    };

    try {

        const response = await fetch("/api/requests", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (!response.ok || !result.success) {
            throw new Error(
                result.message || "Talep gönderilemedi."
            );
        }

        formStatus.className = "form-status success";
        formStatus.textContent = result.message;

        form.reset();

    } catch (error) {

        formStatus.className = "form-status error";
        formStatus.textContent = error.message;

    } finally {

        submitButton.disabled = false;
        submitButton.textContent = "Talep Gönder";
    }
});
