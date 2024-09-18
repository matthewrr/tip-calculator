"use strict";

$(function () {
  var datePicker = document.getElementById('datePicker');
  var picker = new Litepicker({
    element: datePicker,
    format: 'DD MMMM YYYY'
  });
  var dateRangePicker = document.getElementById('dateRangePicker');
  var pickerRange = new Litepicker({
    element: dateRangePicker,
    format: 'DD MMMM YYYY',
    singleMode: false
  });
});