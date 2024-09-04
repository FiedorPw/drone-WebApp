<template>
    <div id="map" ref="map" style="height: 500px; width: 100%"></div>
</template>

<script>
import { Loader } from "@googlemaps/js-api-loader";
// import redDotIcon from "@/assets/markers/red-dot.png";

export default {
    name: "GoogleMap",
    props: {
        // Added props for latitude and longitude
        latitude: {
            type: Number,
            required: true,
        },
        longitude: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            map: null,
            markers: [],
            infoWindow: null,
            currentMarker: null,
        };
    },
    watch: {
        latitude(newLat) {
            this.updateMarker(newLat, this.longitude); // Corrected: use this.longitude
        },
        longitude(newLng) {
            this.updateMarker(this.latitude, newLng); // Corrected: use this.latitude
        },
    },

    mounted() {
        this.initMap();
        // zacznie dodawać randomowe numerki
        this.startAddingRandomMarkers();
    },
    methods: {
        async initMap() {
            const loader = new Loader({
                apiKey: "AIzaSyBFmj02gl59eDUcuwpplc3UY1YcLu8v0Fc", // Replace with your API Key
                version: "weekly",
            });

            await loader.load();

            this.map = new google.maps.Map(this.$refs.map, {
                center: { lat: 52.2297, lng: 21.0122 },
                // center: { lat: this.latitude, lng: this.longitude }, czerpanie środka z pomiarów
                zoom: 8,
            });

            this.infoWindow = new google.maps.InfoWindow();

            this.updateMarker(this.latitude, this.longitude);

            // Emit event that map is ready
            this.$emit("map-ready");
        },
        updateMarker(lat, lng) {
            if (this.currentMarker) {
                // Update position if marker already exists
                this.currentMarker.setPosition({ lat, lng });
            } else {
                // Add new marker if it doesn't exist
                this.currentMarker = this.addMarker({
                    lat,
                    lng,
                    title: "Current Location",
                    content: `Lat: ${lat}, Lng: ${lng}`,
                    // iconUrl: require("@/assets/markers/red-dot.png"),
                    iconUrl: null,
                });
            }
        },
        addMarker({
            lat,
            lng,
            title = "Default Title",
            content = "kontent",
            iconUrl = null,
        }) {
            const marker = new google.maps.Marker({
                position: { lat, lng },
                map: this.map,
                title,
                icon: iconUrl,
            });

            marker.addListener("click", () => {
                this.infoWindow.setContent(content);
                this.infoWindow.open(this.map, marker);
            });

            this.markers.push(marker);
            return marker;
        },

        startAddingRandomMarkers() {
            setInterval(() => {
                const randomLat = 52.2297 + (Math.random() - 0.5) * 0.1;
                const randomLng = 21.0122 + (Math.random() - 0.5) * 0.1;

                var latit = this.latitude / 10000000;
                var longin = this.longitude / 10000000;
                console.log(
                    "lotit:",
                    latit,
                    latit.type,
                    "random lotit:",
                    randomLng,
                    randomLat.type,
                );
                console.log("longin", longin);
                this.addMarker({
                    lat: latit,
                    lng: longin,
                    title: "Pozycja w ",
                    content: "i tak nie działa XD",
                    iconUrl:
                        "https://maps.google.com/mapfiles/ms/icons/red-dot.png",
                });
            }, 1000);
        },
    },
};
</script>

<style scoped>
#map {
    height: 500px;
    width: 100%;
}
</style>
