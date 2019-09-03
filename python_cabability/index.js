$(function(){
	$('.tit-l .tit-l-l-l').on('mouseover',function(){
		$('.tit-x .tit-l-l-l').removeClass('active');
		$(this).addClass('active').siblings().removeClass('active');
		$('.onel .couse-box-ll').eq($(this).index()).addClass('show').siblings().removeClass('show');
		$('.twol .couse-box-ll').removeClass('show');
	})

	$('.tit-x .tit-l-l-l').on('mouseover',function(){
		$('.tit-l .tit-l-l-l').removeClass('active');
		$(this).addClass('active').siblings().removeClass('active');
		$('.twol .couse-box-ll').eq($(this).index()).addClass('show').siblings().removeClass('show');
		$('.onel .couse-box-ll').removeClass('show');
	})

	$('.yuyan-l').on('mouseover',function(){
		$(this).children('.hd-box').stop().animate({
			bottom:-25
		});
	}).on('mouseout',function(){
		$(this).children('.hd-box').stop().animate({
			bottom:-90
		});
	})
})




$(function(){
	$img = $('.box-ddsy img').clone();
	$('.box-ddsy').append($img);
	
	var num = 0;
	/*
	setInterval(()=>{
		num+=10;
		if(num >= 340){
			num=0;
		}
		$('.box-ddsy img').eq(0).animate({
			top:-num
		})
	},30)
	*/
	
})
