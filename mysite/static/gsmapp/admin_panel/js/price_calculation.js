var tbl_pricing = ""

function price_calculation(val){
    if(tbl_pricing == "")
    {
        get_pricing_table(function(output){
            tbl_pricing = output;
            console.log(tbl_pricing);
        });
    }
    
    var facebook_page_cost = 0;
    var instagram_cost = 0;
    var twitter_cost = 0;
    var youtube_cost = 0;
    var linkedin_cost = 0;
    var facebook_total_account = 0;
    var instagram_total_account = 0;
    var youtube_total_account = 0;
    var twitter_total_account = 0;
    var linkedin_total_account = 0;

    var total_user = parseInt($("#kt_nouislider_user_input").val().replace(/[^0-9]/g,''))
    var total_month = parseInt($("#kt_nouislider_duration_input").val().replace(/[^0-9]/g,''))
    
    try{
        if($("#facebook_page_cost").html() != undefined)
        {         
            facebook_total_account = parseInt($("#kt_nouislider_facebook_page_input").val().replace(/[^0-9]/g,''));
            facebook_page_cost = parseInt($("#facebook_page_cost").attr('data-monthly-price')) * facebook_total_account; 
            $("#facebook_page_cost").attr("data-total-account", facebook_total_account).html(facebook_page_cost);  
        }
    }catch{}

    try{
        if($("#instagram_cost").html() != undefined)
        {       
            instagram_total_account = parseInt($("#kt_nouislider_instagram_account_input").val().replace(/[^0-9]/g,''));            
            instagram_cost = parseInt($("#instagram_cost").attr('data-monthly-price')) * instagram_total_account;
            $("#instagram_cost").attr("data-total-account", instagram_total_account).html(instagram_cost);
        } 
    }catch{}

    try{
        if($("#twitter_cost").html() != undefined)
        {           
            twitter_total_account = parseInt($("#kt_nouislider_twitter_account_input").val().replace(/[^0-9]/g,''));    
            twitter_cost = parseInt($("#twitter_cost").attr('data-monthly-price')) * twitter_total_account;
            $("#twitter_cost").attr("data-total-account", twitter_total_account).html(twitter_cost); 
        }  
    }catch{}

    try{
        if($("#youtube_cost").html() != undefined)
        {           
            youtube_total_account = parseInt($("#kt_nouislider_youtube_account_input").val().replace(/[^0-9]/g,''));
            youtube_cost = parseInt($("#youtube_cost").attr('data-monthly-price')) * youtube_total_account;
            $("#youtube_cost").attr("data-total-account", youtube_total_account).html(youtube_cost);
        }           
    }catch{}

    try{
        if($("#linkedin_cost").html() != undefined)
        {         
            linkedin_total_account = parseInt($("#kt_nouislider_linkedIn_account_input").val().replace(/[^0-9]/g,''));
            linkedin_cost = parseInt($("#linkedin_cost").attr('data-monthly-price')) * linkedin_total_account;
            $("#linkedin_cost").attr("data-total-account", linkedin_total_account).html(linkedin_cost);
        }  
    }catch{}

    var grand_total_cost = (facebook_page_cost+instagram_cost+twitter_cost+youtube_cost+linkedin_cost)
    $("#grand_total_div").html(grand_total_cost*total_month);
    $("#total_user_div").html(total_user);
    $("#total_month_div").html(total_month);

    if(total_user==1 && total_month ==1 && facebook_total_account <=2 && instagram_total_account <=2 && youtube_total_account <=2 && twitter_total_account <=2 && linkedin_total_account <=2){
        $("#package_trial_use").show();
    }
    else{
        $("#package_trial_use").hide();
    } 
}

function get_pricing_table(handleData){
    $.ajax({
        url: '/business/get-pricing-table-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            handleData(data);
        }
    });
}