var words = [];

populatePresidents = function() {
  document.getElementById('president').innerHTML="<option value='' selected='selected'>Choose a President</option>";
  var president_counter = 1;
  var presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Buren', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama'];
  for (var i = 0; i < presidents.length; i++) {
    if (i < 10) {
      presidents[i] = "0" + String(i) + presidents[i];
    }
    else {
      presidents[i] = String(i) + presidents[i];
    }

  }
  for (var i = 0; i < presidents.length; i++) {
    if (presidents[i].slice(2) === "Tyler" || presidents[i].slice(2) === "Arthur") {
      president_counter = president_counter + 1
    }
    if (president_counter < 10){
      counter_string = "0" + String(president_counter)
    }
    else {
      counter_string = String(president_counter)
    }
    var pres_string = counter_string + " - " + presidents[i].slice(2);
    new_html = "<option value="+presidents[i]+">"+pres_string+"</option><br>";
    document.getElementById('president').innerHTML = document.getElementById('president').innerHTML + new_html;
    president_counter += 1;
  }
  $('#term').hide();
}

populateTerms = function() {
  document.getElementById('term').innerHTML="<option value='' selected='selected'>All terms</option>";
  if (document.getElementById('president').value === '') {
    $('#term').hide();
    $('#wordcloud').empty();
  }
  else {
    $('#term').show();
    var terms = [[179001, 179012, 179110, 179211, 179312, 179411, 179512, 179612], [179711, 179812, 179912, 180011], [180112, 180212, 180310, 180411, 180512, 180612, 180710, 180811], [180911, 181012, 181111, 181211, 181312, 181409, 181512, 181612], [181712, 181811, 181912, 182011, 182112, 182212, 182312, 182412], [182512, 182612, 182712, 182812], [182912, 183012, 183112, 183212, 183312, 183412, 183512, 183612], [183712, 183812, 183912, 184012], [184112, 184212, 184312, 184412], [184512, 184612, 184712, 184812], [184912], [185012, 185112, 185212], [185312, 185412, 185512, 185612], [185712, 185812, 185912, 186012], [186112, 186212, 186312, 186412], [186512, 186612, 186712, 186812], [186912, 187012, 187112, 187212, 187312, 187412, 187512, 187612], [187712, 187812, 187912, 188012], [188112, 188212, 188312, 188412], [188512, 188612, 188712, 188812], [188912, 189012, 189112, 189212], [189312, 189412, 189512, 189612], [189712, 189812, 189912, 190012], [190112, 190212, 190312, 190412, 190512, 190612, 190712, 190812], [190912, 191012, 191112, 191212], [191312, 191412, 191512, 191612, 191712, 191812, 191912, 192012], [192112, 192212], [192312, 192412, 192512, 192612, 192712, 192812], [192912, 193012, 193112, 193212], [193401, 193501, 193601, 193701, 193801, 193901, 194001, 194101, 194201, 194301, 194401, 194501], [194601, 194701, 194801, 194901, 195001, 195101, 195201, 195301], [195302, 195401, 195501, 195601, 195701, 195801, 195901, 196001, 196101], [196101, 196201, 196301], [196401, 196501, 196601, 196701, 196801, 196901], [197001, 197101, 197201, 197302, 197401], [197501, 197601, 197701], [197801, 197901, 198001, 198101], [198201, 198301, 198401, 198502, 198602, 198701, 198801], [198902, 199001, 199101, 199201], [199302, 199401, 199501, 199601, 199702, 199801, 199901, 200001], [200102, 200109, 200201, 200301, 200401, 200502, 200601, 200701, 200801], [200902, 201001, 201101, 201201, 201302, 201401, 201501, 201601]];
    var current_pres = document.getElementById('president').value;
    var index = parseInt(current_pres.slice(0,2));
    for (var i = 0; i < terms[index].length; i++) {
      var year = parseInt(terms[index][i].toString().slice(0,4));
      var month_num = parseInt(terms[index][i].toString().slice(4));
      var month_str = "";
      if (month_num === 1) {
        month_str = "January";
      }
      else if (month_num === 2) {
        month_str = "February";
      }
      else if (month_num === 3) {
        month_str = "March";
      }
      else if (month_num === 4) {
        month_str = "April";
      }
      else if (month_num === 5) {
        month_str = "May";
      }
      else if (month_num === 6) {
        month_str = "June";
      }
      else if (month_num === 7) {
        month_str = "July";
      }
      else if (month_num === 8) {
        month_str = "August";
      }
      else if (month_num === 9) {
        month_str = "September";
      }
      else if (month_num === 10) {
        month_str = "October";
      }
      else if (month_num === 11) {
        month_str = "November";
      }
      else if (month_num === 12) {
        month_str = "December"
      }
      else {
        month_str = "error"
      }
      var term_string = month_str + " " + year
      var new_html = "<option value="+String(terms[index][i])+">"+term_string+"</option><br>";
      document.getElementById('term').innerHTML = document.getElementById('term').innerHTML + new_html;
    }
  }
}

loadCloud = function() {
  $('#wordcloud').empty();
  var president = document.getElementById('president').value;
  var term = document.getElementById('term').value;
  if (term === '') {
    var filename = 'JSON/' + president + '.json'
  }
  else {
    var filename = 'JSON/' + term + '_' + president.slice(2) + '.json'
  }
  console.log(filename)
  words = [];

  d3.json(filename, function(data) {
    console.log(data)
    for (i = 0; i < data.length; i++) {
      words.push(data[i])
    }
    drawCloud();
  });

}

drawCloud = function () {
  words.sort(function(a,b) {return (a.size < b.size) ? 1 : ((b.size < a.size) ? -1 : 0);} );

  d3.wordcloud()
    .size([800, 400])
    .fill(d3.scale.ordinal().range(["#884400", "#448800", "#888800", "#444400"]))
    .words(words)
    .onwordclick(function(d, i) {
      if (d.href) { window.location = d.href; }
    })
    .start();
}
