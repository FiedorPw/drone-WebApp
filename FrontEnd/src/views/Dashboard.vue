<template>
  <main class="dashboard-page">
    <h1>Dashboard</h1>
    <div class="dashboard">
      <div class="map"></div>
      <div class="container1">
        <div class="camera"></div>
        <div class="container2">
          <div class="info">
            <p class="informacja">Informacja1</p>
            <p class="informacja">Informacja2</p>
            <p class="informacja">Informacja3</p>
            <p class="informacja">Informacja4</p>
            <p class="informacja">Informacja5</p>
            <p class="informacja">Informacja6</p>
            <p class="informacja">Informacja1</p>
            <p class="informacja">Informacja2</p>
            <p class="informacja">Informacja3</p>
            <p class="informacja">Informacja4</p>
            <p class="informacja">Informacja5</p>
            <p class="informacja">Informacja6</p>
          </div>
          <div class="buttons">
            <div class="button">
              <span class="material-icons"> thumb_up </span>
            </div>
            <div class="button">
              <span class="material-icons"> login </span>
            </div>
            <div class="button">
              <span class="material-icons"> report_problem </span>
            </div>
            <div class="button">
              <span class="material-icons"> open_in_full </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
main {
  color: var(--light);
  margin: 0;
  padding: 0;
  width: 100vh;
  height: 100vw;
  background-color: var(--background);
  text-align: center;
  display: flex;
  flex-direction: column;

  .dashboard {
    display: flex;
    flex-direction: row;

    .map {
      margin: 1rem;
      height: 90vh;
      width: 52rem;
      background-image: url("https://budujemydom.pl/i/2023/03/17/442134-35fc-1600x0_google-04.jpg");
      border-radius: 1rem;
    }

    .container1 {
      .camera {
        margin: 1rem;
        height: 50vh;
        width: 40rem;
        background-image: url("https://thumbs.dreamstime.com/b/drone-thermal-night-vision-view-terrorists-camera-zooming-military-drone-night-vision-thermal-view-terrorists-146595612.jpg");
        background-position: center;
        border-radius: 1rem;
      }
      .container2 {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        .info {
          // opacity: 0.1;
          margin: 1rem;
          height: 35.5vh;
          width: 22rem;
          background-color: #000;
          border-radius: 1rem;
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: space-evenly;
          flex-wrap: wrap;
          color: #fff;
          .informacja {
            width: 7rem;
          }
        }
        .buttons {
          margin: 1rem;
          height: 35.5vh;
          width: 16rem;
          background-color: var(--dark-alt);
          border-radius: 1rem;

          display: flex;
          flex-direction: row;
          flex-wrap: wrap;
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
          }
        }
      }
    }
  }
}
</style>
