let MovieObject = {
    init: function(){
    },
    getall : function(){
        $.ajax({
        // 실행할 코드
            type:"GET",
            url:"http://localhost:8000/all"
        }).done(function(response){
        // 성공코드
            console.log(response)
            movielist = response.result

            // topdiv = document.createElement("div")
            // topdiv.style = "column-count: 5"
            // document.body.appendChild(topdiv)

            topdiv = document.getElementById("alldiv")


            movielist.forEach(movie => {
                cmovie = document.createElement("div")
                cmovie.className = "card"

                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.style.cursor = "pointer";

                mimg.onclick = function(){
                    window.open(movie.url);
                }
                // mimg.onmouseover = function(){
                //     mimg.style.cursor = "pointer"
                // }
                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            })

        }).fail(function(response){
        // 실패코드
            console.log(response)
        });
    },
        getgenres : function(){
            const genresel = document.getElementById("sgenre");
            const select = genresel.value;
            //genre = document.getElementById("sgenre").value.toLowerCase()
            $.ajax({
            // 실행할 코드
                type:"GET",
                // url:`http://localhost:8000/genresbest/${genre}`
                url: `http://localhost:8000/genresbest/${select}`

            }).done(function(response){
            // 성공코드
                console.log(response)
                movielist = response.result

                // topdiv = document.createElement("div")
                // topdiv.style = "column-count: 5"
                // document.body.appendChild(topdiv)

                topdiv = document.getElementById("genrediv")
                // topdiv.innerHTML = ""; // 기존영화내용을 없애는 첫번쨰 방법
                while(topdiv.firstChild){                           // 두번쨰 방법
                    topdiv.removeChild(topdiv.firstChild);
                }

                movielist.forEach(movie => {
                    cmovie = document.createElement("div")
                    cmovie.className = "card"

                    mimg = document.createElement("img")
                    mimg.className = "card-img-top"
                    mimg.src = movie.poster_path
                    mimg.style.cursor = "pointer";

                    mimg.onclick = function(){
                        window.open(movie.url);
                    }
                    // mimg.onmouseover = function(){
                    //     mimg.style.cursor = "pointer"
                    // }
                    cmovie.appendChild(mimg)
                    topdiv.appendChild(cmovie)
                })

            }).fail(function(response){
            // 실패코드
                console.log(response)
            });
        }
}

MovieObject.init();
MovieObject.getall();