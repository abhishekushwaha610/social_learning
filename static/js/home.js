// Carousel Controllers
left = $('#left')
right = $('#right')
carousel = $(".videoca")[0]
i = 0 

left.click(
    function () {
        if(carousel.offsetLeft<0){
            
            i +=100;
            console.log("working")
            console.log(carousel.style.marginLeft)
            carousel.style.marginLeft =  i +'px';
        }
        
    }
)

right.click(
    function () {
        if(carousel.offsetLeft > -500){
        i -=100
        console.log(carousel.style.marginLeft)
        carousel.style.marginLeft = i +'px' ;
        }
    }
)

