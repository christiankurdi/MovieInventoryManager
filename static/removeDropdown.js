/*Christian Kurdi
Version: 0.1
*/
showCurrent();
async function showCurrent(){
    const response = await fetch('/getCurrentMovies');
    const data = await response.json();

    data.sort((a, b) => a[0].localeCompare(b[0]));//Sort Alphabetically

    const moviesDropdown = document.getElementById("movieDropdown");

    if(data){
        for(let i = 0;i<data.length;i++){
            //Code to dynamically create movies in removeMovies.html
            const movieOption = document.createElement("option");
            movieOption.textContent = data[i];
            movieOption.value = String(data[i]);
            moviesDropdown.appendChild(movieOption);
        }
    }else{
        moviesDropdown.textContent="Error";
    }
}