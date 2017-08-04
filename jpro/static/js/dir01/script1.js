/**
 * Created by ab01 on 7/8/2017.
 */

$(document).ready(function(){
    $(document).on("click", "#eventsTable2 tr", function(e) {
        console.log(this.childNodes[0].innerText);

           $.ajax({
       url: "/get_scipt/",
       type: 'GET',
       data: {
         'matches_id': this.childNodes[0].innerText,
         'csrftoken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
       },
       success: function (json) {
           console.log('Hi all');
           if (json!='None') {
              json=JSON.parse(json);
   var container = document.getElementById('container03');
   container.innerHTML = json;

           }
           else
               alert("No data");
        }
    });

    });

   $("#button01").click(function(){

   $.ajax({
       url: "/get_scipt/",
       type: 'GET',
       data: {
         'par1': 'obana',
         'csrftoken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
       },
       success: function (json) {
           if (json!='None') {
              json=JSON.parse(json);
   var container = document.getElementById('container02');
    createTree(container, json);
           }
           else
               alert("No data");
        }
    });

   });

function createTree(container, obj) {
  container.innerHTML = createTreeText(obj);
}


function createTreeText(obj) { // отдельная рекурсивная функция
   let tbL = '';
   console.log('length= '+obj.length);

//if (obj.hasOwnProperty(key)) {
   for (var key in obj) {
      let getl =obj[key];
      tbL += '<tr"><td style="display:none;">'+getl['matches_id']+'</td>' + // style=".selected{ background: silver;}
          '<td>' + (key*1+1) +'</td><td>'+ getl['param5'] + '</td></tr>';
    }

   if (tbL) {//style="cursor:pointer"
       var ul = '<table id="eventsTable2" style="cursor:pointer"' +//
           ' class="table table-hover" class="table-condensed table-striped" >'+
     tbL + '</table>';
         // let div01 = document.getElementsByClassName("div01");
         // div01.container02.style.overflow = 'auto'
         // div01.class.overflow //='scroll'
   }

     return ul || '';
 }

});

//============================================================
/*
//    $(function () {
 //   var $result = $('#eventsResult');

    $('#eventsTable').on('all.bs.table', function (e, name, args) {
        console.log('Event:', name, ', data:', args);
    })
    .on('click-row.bs.table', function (e, row, $element) {
        console.log('Event: click-row.bs.table');
    })
    .on('dbl-click-row.bs.table', function (e, row, $element) {
        console.log('Event: dbl-click-row.bs.table');
    })
    .on('sort.bs.table', function (e, name, order) {
        console.log('Event: sort.bs.table');
    })
    .on('check.bs.table', function (e, row) {
        console.log('Event: check.bs.table');
    })
    .on('uncheck.bs.table', function (e, row) {
        console.log('Event: uncheck.bs.table');
    })
    .on('check-all.bs.table', function (e) {
        console.log('Event: check-all.bs.table');
    })
    .on('uncheck-all.bs.table', function (e) {
        $result.text('Event: uncheck-all.bs.table');
    })
    .on('load-success.bs.table', function (e, data) {
        console.log('Event: load-success.bs.table');
    })
    .on('load-error.bs.table', function (e, status) {
        console.log('Event: load-error.bs.table');
    })
    .on('column-switch.bs.table', function (e, field, checked) {
        console.log('Event: column-switch.bs.table');
    })
    .on('page-change.bs.table', function (e, number, size) {
        console.log('Event: page-change.bs.table');
    })
    .on('search.bs.table', function (e, text) {
        console.log('Event: search.bs.table');
    });
//});
*/
