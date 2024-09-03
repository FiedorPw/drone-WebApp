<template>
    <main class="dashboard-page">
        <h1>Dashboard</h1>
        <div class="dashboard">
            <!-- Status Panel -->
            <div class="status-panel">
                <div class="status-info">
                    <p>
                        roll, pitch, yaw<br />{{
                            telemetryData
                                ? `${telemetryData.Roll[0]}°, ${telemetryData.Pitch[0]}°, ${telemetryData.Yaw[0]}°`
                                : "---"
                        }}
                    </p>
                    <p>
                        latitude longitude altitude<br />{{
                            telemetryData
                                ? `${telemetryData.Latitude[0]}, ${telemetryData.Longitude[0]}, ${telemetryData.Altitude[0]}m`
                                : "---"
                        }}
                    </p>
                    <p>
                        HDOP VDOP<br />{{
                            telemetryData
                                ? `${telemetryData.HDOP[0]}%, ${telemetryData.VDOP[0]}%`
                                : "---"
                        }}
                    </p>
                    <p>
                        Satellites<br />{{
                            telemetryData ? telemetryData.Satellites[0] : "---"
                        }}
                    </p>
                    <p>
                        Flight Mode<br />{{
                            telemetryData ? telemetryData.Flight_Mode[0] : "---"
                        }}
                    </p>
                    <p>
                        Voltage<br />{{
                            telemetryData
                                ? `${telemetryData.Voltage[0]}V`
                                : "---"
                        }}
                    </p>
                    <p>
                        Current<br />{{
                            telemetryData
                                ? `${telemetryData.Current[0]}A`
                                : "---"
                        }}
                    </p>
                    <p>
                        Armed<br />{{
                            telemetryData
                                ? telemetryData.Armed[0]
                                    ? "yes"
                                    : "no"
                                : "---"
                        }}
                    </p>
                </div>
            </div>

            <!-- Main Image -->
            <div class="main-image">
                <img
                    src="~@/assets/placeholdery/camera_placeHolder.jpg"
                    alt="Main View"
                />
            </div>

            <!-- Buttons Panel -->
            <div class="buttons-panel">
                <div class="button">
                    <span class="material-icons">thumb_up</span>
                </div>
                <div class="button">
                    <span class="material-icons">login</span>
                </div>
                <div class="button">
                    <span class="material-icons">report_problem</span>
                </div>
                <div class="button">
                    <span class="material-icons">open_in_full</span>
                </div>
            </div>

            <!-- Google Map -->
            <div id="map" class="google-map"></div>
        </div>
    </main>
</template>

<script>
export default {
    data() {
        return {
            data: null,
            loading: false,
            error: null,
            telemetryData: null,
            map: null,
            marker: null,
        };
    },
    methods: {
        async fetchData() {
            this.loading = true;
            this.error = null;
            try {
                const response = await fetch(
                    "http://localhost:5000/api/telemetria",
                );
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                this.data = await response.json();
            } catch (e) {
                this.error = e.message;
            } finally {
                this.loading = false;
            }
        },
        async fetchTelemetry() {
            try {
                const response = await fetch(
                    "http://127.0.0.1:5000/api/telemetry",
                    {
                        mode: "cors",
                        headers: {
                            "Access-Control-Allow-Origin": "*",
                        },
                    },
                );
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                this.telemetryData = await response.json();
                this.updateMapMarker();
            } catch (error) {
                console.error("Error fetching telemetry:", error);
            }
        },
        initMap() {
            this.map = new google.maps.Map(document.getElementById("map"), {
                center: { lat: 0, lng: 0 },
                zoom: 15,
            });
            this.marker = new google.maps.Marker({
                position: { lat: 0, lng: 0 },
                map: this.map,
                title: "Drone Location",
            });
        },
        updateMapMarker() {
            if (this.telemetryData) {
                const latitude = this.telemetryData.Latitude[0];
                const longitude = this.telemetryData.Longitude[0];
                const position = { lat: latitude, lng: longitude };
                console.log(position);

                // Update the map's center and marker position
                this.map.setCenter(position);
                this.marker.setPosition(position);
            }
        },
    },
    mounted() {
        // Load Google Maps script and initialize map
        const googleMapsScript = document.createElement("script");
        googleMapsScript.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyBFmj02gl59eDUcuwpplc3UY1YcLu8v0Fc&callback=initMap`;
        googleMapsScript.async = true;
        window.initMap = this.initMap; // Bind the initMap function to the window object
        document.head.appendChild(googleMapsScript);

        this.fetchData();
        this.fetchTelemetry();
    },
};
</script>

<style lang="scss" scoped>
.dashboard-page {
    color: var(--light);
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 100vh;
    background-color: var(--background);
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;

    h1 {
        margin-bottom: 1rem;
    }

    .dashboard {
        display: grid;
        grid-template-columns: 1fr 2fr;
        grid-template-rows: auto auto;
        gap: 10px;
        padding: 20px;
        width: 100%;
        max-width: 1200px;

        .status-panel {
            grid-column: 1 / 2;
            grid-row: 1 / 2;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #e0e8e5;
            padding: 10px;
            border-radius: 1rem;
        }

        .status-info {
            font-size: 14px;
            line-height: 1.5;
            color: black;
        }

        .main-image {
            grid-column: 2 / 3;
            grid-row: 1 / 2;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #000;
            border-radius: 1rem;
        }

        .main-image img {
            width: 100%;
            height: auto;
            border-radius: 1rem;
        }

        .buttons-panel {
            grid-column: 1 / 2;
            grid-row: 2 / 3;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: space-around;
            padding: 10px;
            background-color: var(--dark-alt);
            border-radius: 1rem;

            .button {
                opacity: 0.5;
                margin: 0.5rem;
                width: 7rem;
                height: 7rem;
                background-color: #000;
                border-radius: 0.5rem;
                transition: 0.3s;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;

                &:hover {
                    opacity: 1;
                    background-color: #333;
                }

                .material-icons {
                    color: #fff;
                }
            }
        }

        .google-map {
            grid-column: 2 / 3;
            grid-row: 2 / 3;
            height: 100%;
            border-radius: 1rem;
        }

        #map {
            width: 100%;
            height: 100%;
            border-radius: 1rem;
        }
    }
}
</style>
