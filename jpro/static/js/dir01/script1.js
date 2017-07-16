/**
 * Created by ab01 on 7/8/2017.
 */

    function createTree(container, obj) {
      container.innerHTML = createTreeText(obj);
    }

    function createTreeText(obj) { // отдельная рекурсивная функция
      let tbL = '';
      console.log('length= '+obj.length);

//if (obj.hasOwnProperty(key)) {
    for (var key in obj) {
       let getl =obj[key];
       tbL += '<tr><td style="display:none;">'+getl['id']+'</td><td>' + key +'</td><td>'+ getl['param5'] + '</td></tr>';
     }

/*
      for (var key in obj) {
        li += '<li>' + key + createTreeText(obj[key]) + '</li>';
      }
*/
      if (tbL) {
        var ul = '<table>' + tbL + '</table>';
          let div01 = document.getElementsByClassName("div01");
          div01.container02.style.overflow = 'scroll'
         // div01.class.overflow //='scroll'
      }

      return ul || '';
    }



function botton01() {
var json_M='{"param5": "$80,000+H OLOMOUC", "started": "1500121908", "ended": null}';
 $.ajax({
        url: "/get_scipt/",
        type: 'GET',
        data: {
          'par1': 'obana',
          'csrftoken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
        },

        success: function (json) {
            if (json!='None') {
                console.log('--------');
               json=JSON.parse(json);
 //               console.dir(json);
//    $('#table').bootstrapTable({
//		data: json_M
//	})
     var container = document.getElementById('container02');
     createTree(container, json);
            }
            else
                alert("No data");

        }
    });

}