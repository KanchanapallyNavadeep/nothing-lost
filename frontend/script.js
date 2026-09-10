async function submitLostItem(event) {

    event.preventDefault();

    const status =
        document.getElementById("statusMessage");

    status.innerHTML =
        "🤖 AI is analyzing the lost item...";


    // Get the selected image file
    const imageFile =
        document.getElementById("lostImage").files[0] || null;


    // Create multipart form data
    const formData = new FormData();


    formData.append(
        "description",
        document.getElementById("lostDescription").value
    );


    formData.append(
        "category",
        document.getElementById("lostCategory").value
    );


    formData.append(
        "color",
        document.getElementById("lostColor").value
    );


    formData.append(
        "latitude",
        document.getElementById("lostLatitude").value
    );


    formData.append(
        "longitude",
        document.getElementById("lostLongitude").value
    );


    // Add image if selected
    if (imageFile) {

        formData.append(
            "image",
            imageFile
        );
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/match",
            {
                method: "POST",
                body: formData
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                "Backend request failed"
            );
        }


        console.log(
            "AI MATCH RESULTS:",
            data
        );


        displayMatches(
            data.matches
        );


    } catch (error) {

        console.error(
            "LOST ITEM ERROR:",
            error
        );


        status.innerHTML =
            "❌ Could not connect to the AI backend.";
    }
}



function displayMatches(matches) {

    const status =
        document.getElementById("statusMessage");


    if (!matches || matches.length === 0) {

        status.innerHTML = `
            <div class="no-match">

                <h2>😔 No matches found</h2>

                <p>
                    We couldn't find a possible match
                    for this item yet.
                </p>

            </div>
        `;

        return;
    }


    let html = `

        <div class="results-container">

            <div class="results-heading">

                <span>
                    AI MATCH RESULTS
                </span>

                <h2>
                    Possible matches found
                </h2>

                <p>
                    Results are ranked using image,
                    text, location and item attributes.
                </p>

            </div>

    `;


    matches.forEach(
        (match, index) => {

            const percentage =
                (match.final_score * 100)
                .toFixed(2);


            const imagePercentage =
                (match.image_score * 100)
                .toFixed(2);


            const textPercentage =
                (match.text_score * 100)
                .toFixed(2);


            const locationPercentage =
                (match.location_score * 100)
                .toFixed(2);


            const attributePercentage =
                (match.attribute_score * 100)
                .toFixed(2);


            html += `

                <div class="match-card">

                    <div class="match-top">

                        <div>

                            <span class="match-label">

                                ${
                                    index === 0
                                    ? "🏆 BEST MATCH"
                                    : "POSSIBLE MATCH"
                                }

                            </span>


                            <h3>
                                Found Item #${match.id}
                            </h3>


                            <p class="match-description">
                                ${match.description}
                            </p>

                        </div>


                        <div class="final-score">

                            ${percentage}%

                        </div>

                    </div>


                    <div class="score-grid">


                        <div class="score-item">

                            <span>
                                🖼 Image
                            </span>

                            <strong>
                                ${imagePercentage}%
                            </strong>

                        </div>


                        <div class="score-item">

                            <span>
                                📝 Text
                            </span>

                            <strong>
                                ${textPercentage}%
                            </strong>

                        </div>


                        <div class="score-item">

                            <span>
                                📍 Location
                            </span>

                            <strong>
                                ${locationPercentage}%
                            </strong>

                        </div>


                        <div class="score-item">

                            <span>
                                🏷 Attributes
                            </span>

                            <strong>
                                ${attributePercentage}%
                            </strong>

                        </div>


                    </div>

                </div>

            `;
        }
    );


    html += `

        </div>

    `;


    status.innerHTML =
        html;


    status.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}



async function submitFoundItem(event) {

    event.preventDefault();


    // Get the selected found-item image
    const imageFile =
        document.getElementById("foundImage").files[0] || null;


    const status =
        document.getElementById("statusMessage");


    status.innerHTML =
        "📦 Registering found item...";


    // Create multipart form data
    const formData = new FormData();


    formData.append(
        "id",
        document.getElementById("foundId").value
    );


    formData.append(
        "description",
        document.getElementById("foundDescription").value
    );


    formData.append(
        "category",
        document.getElementById("foundCategory").value
    );


    formData.append(
        "color",
        document.getElementById("foundColor").value
    );


    formData.append(
        "latitude",
        document.getElementById("foundLatitude").value
    );


    formData.append(
        "longitude",
        document.getElementById("foundLongitude").value
    );


    // Add the actual image file
    if (imageFile) {

        formData.append(
            "image",
            imageFile
        );
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/found-items",
            {
                method: "POST",

                body: formData
            }
        );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                "Found item registration failed"
            );
        }


        console.log(
            "FOUND ITEM REGISTERED:",
            data
        );


        status.innerHTML = `

            <div class="no-match">

                <h2>
                    ✅ Found item registered
                </h2>

                <p>
                    Item #${data.item.id}
                    has been added to the
                    Nothing Lost system.
                </p>

                ${
                    data.item.image
                    ? `<p>📸 Photo uploaded successfully.</p>`
                    : `<p>⚠️ No photo was uploaded.</p>`
                }

            </div>

        `;


    } catch (error) {

        console.error(
            "FOUND ITEM ERROR:",
            error
        );


        status.innerHTML =
            "❌ Could not register the found item.";
    }

}



function showForm(type) {

    const reportSection =
        document.getElementById("report");


    reportSection.scrollIntoView({

        behavior: "smooth"

    });

}