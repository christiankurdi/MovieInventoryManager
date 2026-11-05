/*Christian Kurdi
Version: 0.1
*/

showMovieInfo();
async function showMovieInfo(){
    const params = new URLSearchParams(window.location.search);
    const name = params.get("name");
    const response = await fetch(`/getMovieInfo?name=${encodeURIComponent(name)}`);
    const data = await response.json();

    /*Populate fields in updateMovie.html with data*/
    document.getElementsByName("nameBox")[0].value = data[0][0];
    document.getElementById("genreBox").value = data[0][1];
    document.getElementsByName("actor1")[0].value = data[0][2];
    document.getElementsByName("actor2")[0].value = data[0][3];
    document.getElementsByName("actor3")[0].value = data[0][4];

    let posessionValue = data[0][5] == 0 ? 1 : 0;//Get possesion value according to database value
    
    //Populate radio button
    const radios = document.getElementsByName("posession");
    for (const r of radios){
        r.checked = (r.value == posessionValue);
    }

    //Update old name for update usage
    document.getElementById("oldName").value = name;

    





}