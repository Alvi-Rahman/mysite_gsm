 $("#chk_tag_category").click(function () {  
    $.ajax({
        url: '/business/tag-category-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_tag_name").click(function () {
    $.ajax({
        url: '/business/tag-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_sentiment").click(function () {
    $.ajax({
        url: '/business/sentiment-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_department").click(function () {
    $.ajax({
        url: '/business/department-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_user_group").click(function () {
    $.ajax({
        url: '/business/user-group-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_canned_messages").click(function () {
    $.ajax({
        url: '/business/canned-messages-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_message_templates").click(function () {
    $.ajax({
        url: '/business/message-templates-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_knowledge_base").click(function () {
    $.ajax({
        url: '/business/knowledge-base-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#chk_relevant").click(function () {
    $.ajax({
        url: '/business/relevant-action-by-ajax/',
        type:"GET",
        dataType: 'json',
        success: function (data) { 
            alert(data);
        }
    });
});
 
$("#package_buy_now").click(function () {
    var facebook_page_cost = 0;
    var facebook_page_total = 0;
    var twitter_cost = 0;
    var twitter_account_total = 0;
    var instagram_cost = 0;
    var instagram_account_total = 0;
    var youtube_cost = 0; 
    var youtube_account_total = 0;
    var linkedin_cost = 0;
    var linkedin_account_total = 0;
 
    try{
        facebook_page_cost = parseInt($("#facebook_page_cost").html());
        if(facebook_page_cost.toString() == "NaN"){
            facebook_page_cost = 0;
        }
        else{  
            facebook_page_total = parseInt($("#facebook_page_cost").attr("data-total-account"));
        }
    }catch{}
    try{
        twitter_cost = parseInt($("#twitter_cost").html());
        if(twitter_cost.toString() == "NaN"){
            twitter_cost = 0;
        }
        else{  
            twitter_account_total = parseInt($("#twitter_cost").attr("data-total-account"));
        }
    }catch{}
    try{
        instagram_cost = parseInt($("#instagram_cost").html()); 
        if(instagram_cost.toString() == "NaN"){
            instagram_cost = 0;
        }
        else{  
            instagram_account_total = parseInt($("#instagram_cost").attr("data-total-account"));
        }
    }catch{}
    try{
        youtube_cost = parseInt($("#youtube_cost").html());
        if(youtube_cost.toString() == "NaN"){
            youtube_cost = 0; 
        }
        else{  
            youtube_account_total = parseInt($("#youtube_cost").attr("data-total-account"));
        }
    }catch{}
    try{  
        linkedin_cost = parseInt($("#linkedin_cost").html());
        if(linkedin_cost.toString() == "NaN"){
            linkedin_cost = 0;
        }
        else{  
            linkedin_account_total = parseInt($("#linkedin_cost").attr("data-total-account"));
        }
    }catch{ } 

    $.ajax({
        url: '/business/package-buy-now-by-ajax/',
        type:"GET",
        dataType: 'json',
        data: { 
            'total_user': $("#total_user_div").html(),
            'total_month': $("#total_month_div").html(),
            'grand_total': $("#grand_total_div").html(),
            'facebook_page_cost': facebook_page_cost,
            'twitter_cost': twitter_cost,
            'instagram_cost': instagram_cost,
            'youtube_cost': youtube_cost,
            'linkedin_cost': linkedin_cost, 
            'facebook_page_total': facebook_page_total,
            'twitter_account_total': twitter_account_total,
            'instagram_account_total': instagram_account_total,
            'youtube_account_total': youtube_account_total,
            'linkedin_account_total': linkedin_account_total,
        },
        success: function (data) { 
            alert(data);
            if(data == "Your package buy successfully"){
                window.location.href = "/business/manage-social-accounts/";
            }
        }
    });
});

 
$("#package_trial_use").click(function () {
    var facebook_page_cost = 0;
    var facebook_page_total = 0;
    var twitter_cost = 0;
    var twitter_account_total = 0;
    var instagram_cost = 0;
    var instagram_account_total = 0;
    var youtube_cost = 0; 
    var youtube_account_total = 0;
    var linkedin_cost = 0;
    var linkedin_account_total = 0;
 
    try{
        facebook_page_cost = parseInt($("#facebook_page_cost").html());
        if(facebook_page_cost.toString() == "NaN"){
            facebook_page_cost = 0;
        }
        else{  
            facebook_page_total = parseInt($("#facebook_page_cost").attr("data-facebook_total"));
        }
    }catch{}
    try{
        twitter_cost = parseInt($("#twitter_cost").html());
        if(twitter_cost.toString() == "NaN"){
            twitter_cost = 0;
        }
        else{  
            twitter_account_total = parseInt($("#twitter_cost").attr("data-twitter_total"));
        }
    }catch{}
    try{
        instagram_cost = parseInt($("#instagram_cost").html()); 
        if(instagram_cost.toString() == "NaN"){
            instagram_cost = 0;
        }
        else{  
            instagram_account_total = parseInt($("#instagram_cost").attr("data-instagram_total"));
        }
    }catch{}
    try{
        youtube_cost = parseInt($("#youtube_cost").html());
        if(youtube_cost.toString() == "NaN"){
            youtube_cost = 0;
            
        }
        else{  
            youtube_account_total = parseInt($("#youtube_cost").attr("data-youtube_total"));
        }
    }catch{}
    try{  
        linkedin_cost = parseInt($("#linkedin_cost").html());
        if(linkedin_cost.toString() == "NaN"){
            linkedin_cost = 0;
        }
        else{  
            linkedin_account_total = parseInt($("#linkedin_cost").attr("data-linkedin_total"));
        }
    }catch{ } 
    
    $.ajax({
        url: '/business/package-trial-use-by-ajax/',
        type:"GET",
        dataType: 'json',
        data: { 
            'facebook_page_cost': facebook_page_cost,
            'twitter_cost': twitter_cost,
            'instagram_cost': instagram_cost,
            'youtube_cost': youtube_cost,
            'linkedin_cost': linkedin_cost, 
            'facebook_page_total': facebook_page_total,
            'twitter_account_total': twitter_account_total,
            'instagram_account_total': instagram_account_total,
            'youtube_account_total': youtube_account_total,
            'linkedin_account_total': linkedin_account_total,
        },
        success: function (data) { 
            alert(data);
            if(data == "Your trial account create successful"){
                window.location.href = "/business/manage-social-accounts/";
            }
        }
    });
});
 

function checkuncheck(class_name){
    if($("."+class_name).prop("checked") == true){
        $(".child-"+class_name).prop("checked", true);
        $(".child-"+class_name).prop("disabled", false);
    }
    else if($("."+class_name).prop("checked") == false){
        $("."+class_name).prop("checked", false);
        $(".child-"+class_name).prop("checked", false);
        $(".child-"+class_name).prop("disabled", true);
    }
}

$("#submit_privilege").click(function(){ 
    var users = new Array(); 
    var permission = new Array(); 

    $('#tbl_user_list tr td').find('input[type="checkbox"]:checked').each(function () {
        users.push(this.id);
    });


    $('#tbl_menu_list tr td').find('input[type="checkbox"]:checked').each(function () {
        permission.push(this.id)
    });
     
    if(users.length>0 && permission.length>0)
    {
        $.ajax({
            url: '/business/set-user-privilege-by-ajax/',
            type:"POST",
            dataType: 'json',
            data: { 
                'users': JSON.stringify(users), 
                'permission': JSON.stringify(permission), 
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            },
            success: function (data) { 
                alert(data);
            }
        });
    }
    else{
        alert("Please select user & menu permission");
    }
    
});

$("#set_agent_privilege").click(function(){ 
    var agent = new Array(); 
    var permission = new Array(); 

    $('#tbl_agent_list tr td').find('input[type="checkbox"]:checked').each(function () {
        agent.push(this.id);
    });

    $('#tbl_social_account_list tr td').find('input[type="checkbox"]:checked').each(function () {
        permission.push(this.id)
    });
     
    if(agent.length>0 && permission.length>0)
    {
        $.ajax({
            url: '/business/set-agent-account-assign-by-ajax/',
            type:"POST",
            dataType: 'json',
            data: { 
                'agent': JSON.stringify(agent), 
                'permission': JSON.stringify(permission), 
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            },
            success: function (data) { 
                alert(data);
            }
        });
    }
    else{
        alert("Please select user & social account permission");
    }
});

$(".checkbox_user_per").change(function(){
    var checked_status = false;
    if($("#"+this.id).prop("checked") == true)
    {
        checked_status = true;
    }
    else{ 
        checked_status = false;
    }
    
    $.ajax({
        url: '/business/update-user-privilege-by-ajax/',
        type:"POST",
        dataType: 'json',
        data: { 
            'prev_id': this.id,  
            'checked_status': checked_status,  
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },
        success: function (data) { 
            alert(data);
        }
    });
});


$(".checkbox_agent_permission").change(function(){
    var checked_status = false;
    if($("#"+this.id).prop("checked") == true)
    {
        checked_status = true;
    }
    else{ 
        checked_status = false;
    }

    $.ajax({
        url: '/business/update-agent-privilege-by-ajax/',
        type:"POST",
        dataType: 'json',
        data: { 
            'prev_id': this.id,  
            'checked_status': checked_status,  
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },
        success: function(data) { 
            alert(data);
        }
    });
});


$("#submit_privilege_group").click(function(){ 
    var permission = new Array(); 

    $('#tbl_permission_list tr td').find('input[type="checkbox"]:checked').each(function () {
        permission.push(this.id)
    });
     
    if(permission.length>0)
    {
        $.ajax({
            url: '/business/create-privilege-group-by-ajax/',
            type:"POST",
            dataType: 'json',
            data: { 
                'user_type': $("#user_type").val(), 
                'permission': JSON.stringify(permission), 
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            },
            success: function (data) { 
                alert(data);
            }
        });
    }
    else{
        alert("Please select user & menu permission");
    }
});

$(".checkbox_privilege_group").change(function(){
    var checked_status = false;
    if($("#"+this.id).prop("checked") == true)
    {
        checked_status = true;
    }
    else{ 
        checked_status = false;
    }
    
    $.ajax({
        url: '/business/update-privilege-group-by-ajax/',
        type:"POST",
        dataType: 'json',
        data: { 
            'prev_id': this.id,  
            'checked_status': checked_status,  
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },
        success: function (data) { 
            alert(data);
        }
    });
});