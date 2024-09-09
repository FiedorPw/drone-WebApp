<template>
    <main class="dashboard-page">
        <h1>Dashboard</h1>
        <div class="dashboard">
            <!-- Status Panel -->
            <div class="status-panel">
                <div class="status-info">
                    <p>
                        <b>roll, pitch, yaw</b><br />{{
                            telemetryData
                                ? `${telemetryData.Roll[0]}°, ${telemetryData.Pitch[0]}°, ${telemetryData.Yaw[0]}°`
                                : "---"
                        }}
                    </p>
                    <p>
                        <b>latitude longitude altitude</b><br />{{
                            telemetryData
                                ? `${(telemetryData.Latitude[0] / 10000000).toFixed(3)}°   ${(telemetryData.Longitude[0] / 10000000).toFixed(3)}°  ${telemetryData.Altitude[0].toFixed(2)}m`
                                : "---"
                        }}
                    </p>
                    <p>
                        <b>HDOP VDOP</b><br />{{
                            telemetryData
                                ? `${telemetryData.HDOP[0].toFixed(3)}%, ${telemetryData.VDOP[0].toFixed(3) * 100}%`
                                : "---"
                        }}
                    </p>
                    <p class="inline-telemetry">
                        <b>Satellites </b
                        >{{
                            telemetryData
                                ? telemetryData.Satellites[0].toFixed(1)
                                : "---"
                        }}
                    </p>
                    <p class="inline-telemetry">
                        <b>Flight Mode</b>
                        {{
                            telemetryData ? telemetryData.Flight_Mode[0] : "---"
                        }}
                    </p>
                    <p class="inline-telemetry">
                        <b>Voltage </b>
                        {{
                            telemetryData
                                ? `${telemetryData.Voltage[0]}V`
                                : "---"
                        }}
                    </p>
                    <p class="inline-telemetry">
                        <b>Current </b
                        >{{
                            telemetryData
                                ? `${telemetryData.Current[0]}A`
                                : "---"
                        }}
                    </p>
                    <p class="inline-telemetry">
                        <b>Armed </b
                        >{{
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
                    v-if="streamAvailable"
                    :src="streamUrl"
                    alt="Live Stream"
                />
                <img
                    src="http://drone.knr.edu.pl/camera/action=stream"
                    alt="Live Camera Stream"
                />
                <!-- src="~@/assets/placeholdery/camera_placeHolder.jpg" alt="Main -->
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
                <!-- debug do sprawdzania dodawania markerów -->
                <!-- <div class="button">
                    <button style="color: white" @click="addMarkerToMap">
                        Add Marker
                    </button>
                </div> -->
            </div>

            <!-- Google Map -->
            <div id="map" class="google-map">
                <GoogleMap
                    ref="googleMap"
                    @map-ready="onMapReady"
                    :latitude="lat"
                    :longitude="lng"
                />
            </div>
        </div>
    </main>
</template>
<script>
import GoogleMap from "../components/GoogleMap.vue";
import yellowDotIcon from "@/assets/yellow-dot.png";

export default {
    name: "dashboard",
    components: {
        GoogleMap,
    },
    data() {
        return {
            data: null,
            loading: false,
            error: null,
            telemetryData: null,
            mapReady: false,
            marker: null,
            lat: 52.2297, // Default latitude
            lng: 21.016, // Default longitude
        };
    },
    methods: {
        async fetchTelemetry() {
            try {
                const response = await fetch(
                    "https://dron.knr.edu.pl/api",
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
                this.telemetryData = await response.json(); // call as a function

                this.lat = parseFloat(this.telemetryData.Latitude[0]);
                this.lng = parseFloat(this.telemetryData.Longitude[0]);
            } catch (error) {
                console.error("Error fetching telemetry:", error);
            }
        },

        startTelemetryFetch(interval = 1000) {
            this.fetchTelemetry();
            setInterval(this.fetchTelemetry, interval);
        },
        onMapReady() {
            this.mapReady = true;
            this.startTelemetryFetch();
        },
    },
    mounted() {
        // console.log(this.telemetryData);
        this.startTelemetryFetch();
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
        .inline-telemetry {
            text-align: left;
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
        p {
            font-size: 20px;
        }
    }
}
</style>
