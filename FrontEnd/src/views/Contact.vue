<template>
    <main class="contact-page">
        <h1>Kontakt</h1>
        <p>Zeby cos było</p>
        <p v-if="telemetryData">HDOP: {{ telemetryData.HDOP[0] }}</p>
        <p v-else>HDOP: ---</p>
    </main>
</template>

<script>
export default {
    data() {
        return {
            telemetryData: null,
        };
    },
    mounted() {
        this.fetchTelemetry();
    },
    methods: {
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
                console.log(this.telemetryData);
            } catch (error) {
                console.error("Error fetching telemetry:", error);
            }
        },
    },
};
</script>
