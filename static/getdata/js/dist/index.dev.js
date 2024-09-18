"use strict";

function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance"); }

function _iterableToArrayLimit(arr, i) { if (!(Symbol.iterator in Object(arr) || Object.prototype.toString.call(arr) === "[object Arguments]")) { return; } var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }

//should i continuously feed into dictionary?
$(document).ready(function () {
  $('.employee-select').select2({
    placeholder: "Employee",
    theme: "bootstrap-5"
  }); //better way to code

  $("#start-date").datepicker({
    dateFormat: "d m yy" // dateFormat: "D M d yy",

  });
  $("#end-date").datepicker({
    dateFormat: "d m yy" // dateFormat: "D M d yy"

  });
  $(function () {
    $("#start-date").datepicker("setDate", "-1");
    $("#end-date").datepicker("setDate", "0");
  });
}); // Delete row

$('#employee-rows').on('click', '.btn-delete', function () {
  $(this).parent().parent().remove();
}); // Add Employee Row

$('#add-employee').on('click', function (e) {
  var toAppend = $(".row-employee-hidden").clone();
  toAppend.addClass("row-employee").removeClass('d-none row-employee-hidden');
  $("#employee-rows").append(toAppend);
  $(".employee-select-hidden").removeClass("employee-select-hidden").addClass('employee-select');
  $(".employee-select").last().select2({
    placeholder: "Employee",
    theme: "bootstrap-5"
  });
});
$('#employee-rows').on('change', '.employee-select', function () {
  var role = $(this).find(':selected').attr('class');
  $(this).parent().parent().find('.role-select').val(role);
  var empID = $(this).find(':selected').attr('data');
  $(this).parent().parent().attr('id', empID);
}); // Validate/Invalidate Button

$('#employee-rows').on('blur change', '.user-input', function () {
  var isValid = true;
  var row = $(this).parent().parent();
  var userInputs = row.find('.blur-input');
  var userSelects = row.find('.blur-select');
  $(userInputs).each(function () {
    if ($(this).val() === '' || $(this).hasClass("is-invalid")) {
      isValid = false;
    }
  });
  $(userSelects).each(function () {
    if ($(this).val() == 'Employee Name' | $(this).val() == 'Role') {
      isValid = false;
    }
  });
  var validBtn = row.find('.btn-valid');

  if (isValid) {
    validBtn.removeClass('btn-secondary').addClass('btn-success').prop("disabled", false);
  } else {
    validBtn.removeClass('btn-success').addClass('btn-secondary').prop("disabled", true);
  }
}); //CHECKING VALIDITY

function checkValidity(el, regex) {
  // add regex to allow blank to eliminate first if parameter
  var isValid = regex.test($(el).val());

  if ($(el).val() && !isValid) {
    el.addClass("is-invalid");
  } else {
    el.removeClass("is-invalid");
  }
} // Note that the following regex allows "1: PM"
// BLUR V CHANGE


var USDollar = new Intl.NumberFormat('en-US', {
  style: "decimal",
  minimumFractionDigits: 2
});
var moneyRegex = /^(\d+|\d{1,3}(,\d{3})*)(\.\d{1,2})?$/;
var timeRegex = /^([1-9]|[1][0-2]):?([0-5]\d)?\s?(?:AM|PM)$/i; //way better way to do this

$('#employee-rows').on('change', '.blur-input', function () {
  checkValidity($(this), timeRegex);
});
$('#rev-column').on('change', '.rev-input', function () {
  checkValidity($(this), moneyRegex);
});
$('#tips-cash').on('change', function (e) {
  checkValidity($(this), moneyRegex);
});
$('#tips-cc').on('change', function (e) {
  checkValidity($(this), moneyRegex);
});
$('#cc-pulled').on('change', function (e) {
  checkValidity($(this), moneyRegex);
});
$('#pull-time').on('change', function (e) {
  checkValidity($(this), timeRegex);
}); //END VALIDITYY

function formatTime(time) {
  var newTime = [];

  var _time$match = time.match(/\d+|\w+/g),
      _time$match2 = _slicedToArray(_time$match, 3),
      hour = _time$match2[0],
      min = _time$match2[1],
      period = _time$match2[2];

  if (!period) {
    newTime = [Number(hour), "00", min.toUpperCase()];
  } else {
    newTime = [Number(hour), min, period.toUpperCase()];
  }

  if (newTime[2] == 'PM' && newTime[0] != 12) {
    newTime[0] += 12;
  } else if (newTime[0] == 12 && newTime[2] == "AM") {
    newTime[0] = 0;
  }

  newTime[0] = newTime[0].toString();

  if (newTime[0].length == 1) {
    newTime[0] = "0" + newTime[0];
  }

  return newTime[0].concat(":", newTime[1]);
} ////////////// START REVENUE //////////////


function updateRevData(totalRev, tipRate) {
  $('#tips-rate').val(tipRate);
  $('#rev-total').val(USDollar.format(totalRev));
}

function findTotalRev() {
  var totalRev = 0;
  var method = $("#rev-select").find('option:selected').val();

  if (method == "cumulative") {
    totalRev = Number($('.rev-input').last().val().replace(/\,/g, ''));
  } else {
    $('.rev-input').each(function () {
      totalRev += Number($(this).val().replace(/\,/g, ''));
    });
  }

  return totalRev;
}

function findHourlyRev() {
  var method = $("#rev-select").find('option:selected').val();
  var hourlyRev = [];

  if (method == "cumulative") {
    $(".rev-input").each(function () {
      var idx = hourlyRev.length - 1;

      if (idx >= 0) {
        var latestHour = Number(hourlyRev[idx][1]); // put into function as 0?

        hourlyRev.push([$(this).prop('name'), Number($(this).val() - latestHour)]);
      } else {
        hourlyRev.push([$(this).prop('name'), Number($(this).val())]);
      }
    });
  } else {
    $(".rev-input").each(function () {
      hourlyRev.push([$(this).prop('name'), $(this).val() || 0]);
    });
  }

  return hourlyRev;
}

function updateRev() {
  var totalRev = findTotalRev();
  var totalTips = Number($('#tips-total').val().replace(/\,/g, ''));
  var tipRate = USDollar.format(totalTips / totalRev * 100);
  updateRevData(totalRev, tipRate);
}

;
$('#rev-all').on('change', '.rev-input', function () {
  updateRev();
});
$("#rev-select").on('change', function () {
  updateRev();
}); ////////////// END REVENUE //////////////

$('.tip-input').on('blur change', function () {
  var totalTips = 0;
  var tipsPulled = Number($('#cc-pulled').val().replace(/\,/g, ''));
  var ccTips = Number($('#tips-cc').val().replace(/\,/g, ''));
  var totalRev = Number($('#rev-total').val().replace(/\,/g, ''));
  $('.tip-input').each(function () {
    totalTips += Number($(this).val().replace(/\,/g, ''));
  });
  $('#percentOnCard').val(USDollar.format(ccTips / totalTips * 100));
  $('#tips-rate').val(USDollar.format(totalTips / totalRev * 100));
  $('#tips-total').val(USDollar.format(totalTips));

  if (tipsPulled) {
    $('#tips-distribute').val(USDollar.format(totalTips - tipsPulled));
  } else {
    $('#tips-distribute').val(USDollar.format(totalTips));
  }
});
$('#cc-pulled').on('blur change', function (e) {
  var totalTips = $('#tips-total').val().replace(/\,/g, '');
  var ccPulled = $(this).val().replace(/\,/g, '');

  if ($(this).val()) {
    $('#tips-distribute').val(USDollar.format(totalTips - ccPulled));
  } else {
    $('#tips-distribute').val(USDollar.format(totalTips));
  }
}); //code for change on either of elements

$('#midshift-toggle :checkbox').change(function () {
  if (this.checked) {
    $('#cc-pulled').prop("disabled", false);
    $('#pull-time').prop("disabled", false);
  } else {
    $('#cc-pulled').prop("disabled", true);
    $('#pull-time').prop("disabled", true);
  }
});
$('#tips-toggle :checkbox').change(function () {
  if (this.checked) {
    $('.tips-rate-role').prop("disabled", false);
  } else {
    $('.tips-rate-tole').prop("disabled", true);
  }
});
$('#shift-valid :checkbox').change(function () {
  if (this.checked) {
    $('#shift-notes').prop("disabled", false);
  } else {
    $('#shift-notes').prop("disabled", true);
  }
});
$('#employee-rows').on('change', '.timecard-input', function () {
  // SET DATA VALUE TO MINUTES WORKED>>> SET EVERYTHING TO DATA VALUES
  var valid = true;
  var parent = $(this).parent().parent();
  var timecardInputs = parent.find('.timecard-input');
  timecardInputs.each(function () {
    if ($(this).val() == '') {
      valid = false;
    }
  });

  if (valid == false) {
    return;
  }

  var start = parent.find(".start-time").val();
  var end = parent.find(".end-time").val();
  start = formatTime(start).split(":");
  end = formatTime(end).split(":");
  var hours = end[0] - start[0];
  var minutes = end[1] - start[1];

  if (hours < 0) {
    hours += 24;
  }

  if (minutes < 0) {
    minutes += 60;
    hours -= 1;
  }

  var minsWorked = hours * 60 + minutes;
  hours = hours.toString();

  if (hours == "0.0") {
    hours = "0";
  }

  minutes = Math.round(minutes / 60 * 100);
  minutes = minutes.toString();

  if (minutes == "0") {
    minutes = "00";
  }

  var hoursWorked = hours.concat(".", minutes); //how about find nearest of class

  var parent = $(this).parent().parent();
  parent.find('.hours-worked').val(hoursWorked).attr("data-mins-worked", minsWorked);
});

function validationErrors(error) {
  // prioritize... for example, hours seem high but name not input. or should I do initial that blocks validate modal?
  var errors = {}; // FATAL

  var fatalErrors = {
    "Incomplete Row": "XXXRow #[x] contains partial information. Please finish or remove all information from the row.",
    "Revenue Method": "XXXYou selected the cumulative method for recording hourly revenue but listed a cumulative revenue at one point as less than the cumulative revenue at an earlier hour.",
    "Tip Rate Error": "XXXThe sum of all tips rates to not add to 100%.",
    "Barback Hours": "The current iteration of the tip calculator requires a barback to be present during all operating hours.",
    "Bartender Hours": "The current iteration of the tip calculator requires a bartender to be present during all operating hours.",
    "Employee Duplicated": "XXX[employee name] was added more than once. The tip calculator does not currently support adding an employee more than once."
  }; // ALERT

  var alertErrors = {
    "Employee Hours Abnormally High": "[employee name]'s hours seem abnormally high. This warning triggers when an individual's hours surpass 10. [employee name] is logged as having worked [x] hours.",
    "Employee Hours Abnormally Low": "[employee name]'s hours seem abnormally low. This warning triggers when an individual's hours are below 1. [employee name] is logged as having worked [x] hours.",
    "Tip Rate Abnormally High": "The tip rate seems abnormlly high at [x]%. This warning triggers when the tip rate exceeds 30%.",
    "Tip Rate Abnormally Low": "The tip rate seems abnormlly low at [x]%. This warning triggers when the tip rate falls below 15%.",
    "Revenue Abnormally High": "The revenue during [x-y] seems abnormally high. This warning is triggers when hourly revenue exceeds [z]."
  };
  var errZeroValue = "";
  var errNegValue = ""; //make sure negative values aren't possible

  return fatalErrors[error]; // <li class="list-group-item">Make sure date is 1-2 (force in-place), does the timeframe make sense</li>
  // <li class="list-group-item">summary of changes including day, change default role, someone working before open </li>
  // <li class="list-group-item">time of pull makes sense</li>
  // <li class="list-group-item">summary of non-used forms</li>
}

$("#validate-timecards5").on("click", function () {
  var data = {};

  function tipRatesAddTo100() {
    var sum = $('#bartender-rate').val() + $('#barback-rate').val() + $('#security-rate').val();

    if (sum == 1) {
      return true;
    } else {
      return false;
    }
  }

  function employeeRows() {
    var errors = {
      "Incomplete Row(s)": false,
      "Duplicate Employee(s)": false,
      "Employee(s) Hours": false
    };
    var activeEmployees = [];
    $(".row-employee").each(function () {
      if ($(this).find(".complete").is(":disabled")) {
        if (!($('.blur-select').val().length() == 0)) {
          errors["Incomplete Row(s)"] = true; //repeat anyway but add the row number
        }
      }

      activeEmployees.push($(this).find('.employee-select').val());
    });
    var duplicates = new Set(activeEmployees).size == activeEmployees.length;
    errors["Duplicate Employee(s)"] = duplicates;
  }

  function revenueMethod() {
    var revenue = [];
    var lastRev = 0;
    $(".rev-input").each(function () {
      if (lastRev > $(this).val()) {
        return false;
      }

      lastRev = $(this).val();
      revenue.push([$(this).prop('name'), $(this).val() || 0]);
    });
    return true;
  }
});
$("#validate-timecards").on("click", function () {
  //will it recognize dynamic?
  //BUILTIN WAYS TO COLLECT FORM DATA?
  var errors = []; //TIPS

  var tipRate = $('#tips-rate').val();
  var tipsByRole = {
    'BARTENDER': Number($('#bartender-rate').val()),
    'BARBACK': Number($('#barback-rate').val()),
    'SECURITY': Number($('#security-rate').val()),
    'OTHER': 0
  };
  var tipsValues = Object.values(tipsByRole);
  var tipsSum = tipsValues.reduce(function (a, v) {
    return a + v;
  }, 0);

  if (tipsSum !== 100) {
    errors.push('tipsSum');
  } //REVENUE


  var revenue = [];
  var activeHours = {};
  var lastRev = 0;
  var revErr = false;
  $(".rev-input").each(function () {
    if (!revErr) {
      if (lastRev > $(this).val()) {
        errors.push('revMethod');
        revErr = true;
      }

      lastRev = $(this).val();
    }

    var hour = $(this).prop('name');
    revenue.push([hour, $(this).val() || 0]);
    activeHours[hour] = 0; //start creating a dynamic (hours worked)... relevant once able to change hours worked
  });
  var hours = {};

  for (var i = 0; i < revenue.length; i++) {
    var rev = revenue[i][1];
    var tips = rev * (tipRate / 100);
    hours[revenue[i][0]] = {
      "revenue": rev,
      "tips": tips,
      "securityMinutes": 0,
      "role": {
        "BARTENDER": {
          "minutesWorked": 0,
          "tipsEarned": 0,
          "tipRate": tipsByRole['BARTENDER'] / 100
        },
        "BARBACK": {
          "minutesWorked": 0,
          "tipsEarned": 0,
          "tipRate": tipsByRole['BARBACK'] / 100
        },
        "SECURITY": {
          "minutesWorked": 0,
          "tipsEarned": 0,
          "tipRate": 0
        }
      }
    };
  }

  var timecards = {};
  $(".row-employee").each(function () {
    //if validate without exiting hours works?...
    var activeEmployees = [];

    if ($(this).find(".complete").is(":disabled")) {
      if (!($('.blur-select').val().length == 0)) {
        var name = $(this).find('.employee-select').val();
        errors.push(["IncompleteRow", name]);
        activeEmployees.push(name);
      } //repeats when unneccesary


      return; //correct way to get out of each??!!!!!!!!!!!!!!!!!
    }

    var duplicates = new Set(activeEmployees).size !== activeEmployees.length;

    if (duplicates) {
      errors.push("DupeEmp");
    }

    var name = $(this).find('.employee-select').val();
    var empID = $(this).attr('id');
    var role = $(this).find('.role-select').val(); //it's including "Role"\\

    var startFormatted = formatTime($(this).find('.start-time').val()).split(":");
    var endFormatted = formatTime($(this).find('.end-time').val()).split(":");
    var start = {
      "hour": startFormatted[0],
      "minute": startFormatted[1]
    };
    var end = {
      "hour": endFormatted[0],
      "minute": endFormatted[1]
    };
    var hrsWorked = $(this).find('.hours-worked').val();

    if (Number(hrsWorked.split(':')[0]) >= 12) {
      errors.push("highHours");
    }

    timecards[empID] = {
      'name': name,
      'role': role,
      'earnings': {
        'wage': 16.28,
        //adjust by role, make editable by admin
        'earningsByHour': activeHours,
        'tipEarnings': "",
        'totalEarnings': "",
        'effectiveHourly': ""
      },
      'hours': {
        'start': start,
        'end': end,
        'minsWorked': $(this).find('.hours-worked').data('mins-worked'),
        //do differently
        'workedByHour': activeHours
      }
    };
  });
  console.log('ERRORS:');
  console.log(errors); //normalize numbers

  var formData = {
    // does 'form' allow me to collect all this automatically/quicker?
    //dynamic rates by user added role
    'submitted': Date.now(),
    'submitter-pk': $('#user-id').data('user'),
    'start-date': $('#start-date').val(),
    'end-date': $('#end-date').val(),
    'tips-cash': $('#tips-cash').val(),
    'tips-cc': $('#tips-cc').val(),
    'tips-rate': tipRate,
    'bartender-rate': $('#bartender-rate').val(),
    'barback-rate': $('#barback-rate').val(),
    'security-rate': $('#security-rate').val(),
    'cc-pulled': $('#cc-pulled').val(),
    'pull-time': $('#pull-time').val(),
    'shift-notes': $('#shift-notes').val(),
    'hours': hours,
    'rev-method': $("#rev-select").find('option:selected').val(),
    //need selected?
    'rev-total': $('#rev-total').val(),
    'rev-hourly': revenue,
    'timecards': timecards
  };

  function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');

      for (var _i2 = 0; _i2 < cookies.length; _i2++) {
        var cookie = cookies[_i2].trim(); // Does this cookie string begin with the name we want?


        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }

    return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');
  $.ajax({
    type: 'POST',
    url: "/validate/",
    data: {
      formData: JSON.stringify(formData)
    },
    headers: {
      'X-CSRFToken': csrftoken
    },
    success: function success(response) {
      var employeeData = response['timecards'];

      for (var _i3 = 0, _Object$entries = Object.entries(employeeData); _i3 < _Object$entries.length; _i3++) {
        var _Object$entries$_i = _slicedToArray(_Object$entries[_i3], 2),
            key = _Object$entries$_i[0],
            value = _Object$entries$_i[1];

        var myID = "#".concat(key);
        var totalTips = Number(value["earnings"]["tipEarnings"]);
        console.log("TOTAL TIPS");
        console.log(totalTips);
        var ccTipRate = Number($('#percentOnCard').val()) / 100;
        console.log(ccTipRate);
        var tipsToReport = ccTipRate * totalTips;
        console.log(tipsToReport); // .tips-to-report

        totalTipsUS = "$" + USDollar.format(totalTips);
        $(myID).find(".tips-earned").val(totalTipsUS);
        tipsToReport = "$" + USDollar.format(tipsToReport);
        $(myID).find(".tips-to-report").val(tipsToReport);
      } // if (response.status === 'success') {
      // } else {alert('Error validating data');
      // }

    },
    error: function error() {
      alert('Error validating data');
    }
  });
}); //how does midnight show after translation?
//test times
// var times = ["3am", "3 am", "3:00am", "3:00 am", "1pm", "2 pm", "3 Pm", "4:00 am", "5:00pm", "2pm",
//              "3:23am", "3:23 am", "3:20am", "3:00 am", "1:20pm", "2:20 pm", "3:20 Pm", "4:20 am", "5:20pm", "2:20pm"
// for (let i = 0; i < times.length; i++) { 
//     console.log(formatTime(times[i]))
// }