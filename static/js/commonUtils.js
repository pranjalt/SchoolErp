
function getClassesValue(batchId){
	$.ajax({
		  method: "GET",
		  url: '/getclassesBySelectedBatch/'+'?batchId='+batchId,
		  data: {},
		  dataType:'json',
		})
		 .done(function( data ) {
			  $('#idClass').prop("disabled", false);
			  $('#idClass').empty();
			  console.log(data);
			  $('#idClasss option:first').text('Please Select').at;		  
			  $.each(data,function(key,value){ 
				  $('#idClass').append('<option value="'+value.batch_class_id+'">'+value.grade.class_field+'</option>'); 
			  });
		  })
		  	  
};

function getSectionValue(batchclassId){
	alert("in ajax funtion getClassValue"+selectedOpt);
	$.ajax({
		  method: "GET",
		  url: '/getsectionBySelectedClass/'+'?batchclassId='+batchclassId,
		  data: {},
		  dataType:'json',
		})
		 .done(function( data ) {
			  console.log(data);
			  $('#idSection').prop("disabled", false);
			  $('#idSection').empty();
			  $("#idSection option:first").text('Please Select');
			  $.each(data,function(key,value){ 
				  	console.log(key + '::' + value.section_info.section)
				  	console.log(value.section_info.section)
			  		$('#idSection').append('<option value="'+value.batch_class_section_id+'">'+value.section_info.section+'</option>');
				  	var section = $("#idSection option:selected").val();		
					$('#bcsId').val(section);
			  });
		  })
		  	  
};


function getResultFucntion(tab_url, bcsId,examTypeId) {
	var data={bcsId:bcsId,examTypeId:examTypeId}
	$.ajax({
		  method: "GET",
		  url: tab_url,
		  data: data,
		})
		  .done(function( msg ){
			console.log(msg);
			$('#idStudResultTable').prop("hidden", false);
			$('#student_results').html(msg);
		  });
};


function getStudentRankingFun(tab_url, bcsId,examTypeId) {
	var data={bcsId:bcsId,examTypeId:examTypeId}
	$.ajax({
		  method: "GET",
		  url: tab_url,
		  data: data,
		})
		  .done(function( msg ){
			console.log(msg);
			$('#idStudRankingTable').prop("hidden", false);
			$('#student_ranking').html(msg);
		  });
};


function getAttendenceResultList(url,data)
{
	alert("In JS");
	alert(data);
	$
	.ajax({
		url : url,
		type : "GET",
		//dataType: "json",
		data : data,
	})
		.done(function( msg ){
			alert(msg);
			console.log(msg);
			$('#AResult').show();
			$('#AResult').html(msg);
			
		});
}





function getRankingDetails(url,data)
{
	alert("In JS");
	alert(data);
	$
	.ajax({
		url : url,
		type : "GET",
		//dataType: "json",
		data : data,
	})
		.done(function( msg ){
			alert(msg);
			console.log(msg);
			$('#AResult').show();
			$('#AResult').html(msg);
			
		});

}