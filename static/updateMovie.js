/*Christian Kurdi
Version: 0.1
*/

showMovieInfo();
async function showMovieInfo(){
    const response = await fetch('/getMovieInfo');
    const data = await response.json();

    /*Populate fields in updateMovie.html with data*/
    document.getElementByName("nameBox")[0].value = data[0];
    document.getElementByID("genreBox").value = data[1];
    document.getElementByName("actor1")[0].value = data[2];
    document.getElementByName("actor2")[0].value = data[3];
    document.getElementByName("actor3")[0].value = data[4];

    let posessionValue = 1;
    if (data[5] == 0){
        posessionValue = 0;
    }
    const radios = document.getElementsByName("posession");
    for (const r of radios){
        r.checked = (r.value == posessionValue);
    }

    





}