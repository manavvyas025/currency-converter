const convertBtn = document.getElementById("convertBtn");

convertBtn.addEventListener("click", async function () {

    const currency = document.getElementById("currency").value;
    const amount = document.getElementById("amount").value;

    const result = document.getElementById("result");

    try {

        const response = await fetch("/convert", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                currency: currency,
                amount: amount
            })
        });


        const data = await response.json();


        if (response.ok) {

            result.innerHTML = `
                <strong>${data.amount} ${data.currency}</strong>
                <br>
                =
                <br>
                <strong>₹${data.converted_amount} INR</strong>
                <br><br>
                Exchange Rate: 1 ${data.currency} = ₹${data.rate}
            `;

        } else {

            result.innerHTML = `
                <span style="color: red;">
                    ${data.error}
                </span>
            `;

        }

    } catch (error) {

        result.innerHTML = `
            <span style="color: red;">
                Unable to connect to the server.
            </span>
        `;

        console.error(error);
    }

});