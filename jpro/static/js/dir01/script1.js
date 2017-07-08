/**
 * Created by ab01 on 7/8/2017.
 */

function botton01() {
    alert('Hi freaks! I really');

    $.ajax({
  url: 'get_scipt',
  type: 'POST',
//  data: { code: code, lan: lang, input1:input1},
  success: function(response) {
    result = JSON.parse(response);
    if (result.error) {
      alert(result.error_text);
    } else {  // Success
       alert("");
//      print 'yes';
    } // end if
    }, //end function
  error: function(data) {
  alert('error: '+data.text);
            }

} // end ajax
);
}