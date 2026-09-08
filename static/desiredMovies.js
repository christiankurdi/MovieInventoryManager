/*Christian Kurdi
Version: 0.1
*/
showCurrent();
async function showCurrent(){
    const response = await fetch('/getDesiredMovies');
    const data = await response.json();

    data.sort((a, b) => a[0].localeCompare(b[0]));//Sort Alphabetically

    const moviesBox = document.getElementById("moviesList");
    
    if(data){
        for(let i = 0;i<data.length;i++){
            //Code to dynamically create movies in currentMovies.html
            const newMovieDiv = document.createElement("div");
            newMovieDiv.className= "movieTitles";
            newMovieDiv.textContent = data[i];
            moviesBox.appendChild(newMovieDiv);
        }
    }else{
        moviesBox.textContent="Error";
    }
}