/* Project specific Javascript goes here. */

//function populateSpeciesList(data) {
//    console.log(data)
//    data.foreach(function(datum) {
//        $('.species-list').append("<li>"+datum.name+"</li>");
//    });
//}

$.ajax({url:"/api/species/"}).done(function (data) {
    console.log(data);
    data.forEach(function(datum) {
        $('.species-list').append("<li>"+datum.full_name+"</li>");
    });
});
