import React, { Component } from 'react';
import fire from './fire';

class App extends Component {
  constructor(props) {
    super(props);
    this.addPresidents = this.addPresidents.bind(this); // <- set up react state
  }
  componentWillMount(){
    /* Create reference to messages in Firebase Database */
    // let messagesRef = fire.database().ref('messages').orderByKey().limitToLast(100);
    // messagesRef.on('child_added', snapshot => {
    //   /* Update React state when message is added at Firebase Database */
    //   let message = { text: snapshot.val(), id: snapshot.key };
    //   this.setState({ messages: [message].concat(this.state.messages) });
    // })
  }
  main() {
    addPresidents(e){
       // <- prevent form submit from reloading the page
      /* Send the message to Firebase */
      var presidents = ['01 - Washington', '02 - Adams', '03 - Jefferson', '04 - Madison', '05 - Monroe', '06 - Adams', '07 - Jackson', '08 - Buren', '10 - Tyler', '11 - Polk', '12 - Taylor', '13 - Fillmore', '14 - Pierce', '15 - Buchanan', '16 - Lincoln', '17 - Johnson', '18 - Grant', '19 - Hayes', '21 - Arthur', '22 - Cleveland', '23 - Harrison', '24 - Cleveland', '25 - McKinley', '26 - Roosevelt', '27 - Taft', '28 - Wilson', '29 - Harding', '30 - Coolidge', '31 - Hoover', '32 - Roosevelt', '33 - Truman', '34 - Eisenhower', '35 - Kennedy', '36 - Johnson', '37 - Nixon', '38 - Ford', '39 - Carter', '40 - Reagan', '41 - Bush', '42 - Clinton', '43 - Bush', '44 - Obama'];
      var terms = [[179001, 179012, 179110, 179211, 179312, 179411, 179512, 179612], [179711, 179812, 179912, 180011], [180112, 180212, 180310, 180411, 180512, 180612, 180710, 180811], [180911, 181012, 181111, 181211, 181312, 181409, 181512, 181612], [181712, 181811, 181912, 182011, 182112, 182212, 182312, 182412], [182512, 182612, 182712, 182812], [182912, 183012, 183112, 183212, 183312, 183412, 183512, 183612], [183712, 183812, 183912, 184012], [184112, 184212, 184312, 184412], [184512, 184612, 184712, 184812], [184912], [185012, 185112, 185212], [185312, 185412, 185512, 185612], [185712, 185812, 185912, 186012], [186112, 186212, 186312, 186412], [186512, 186612, 186712, 186812], [186912, 187012, 187112, 187212, 187312, 187412, 187512, 187612], [187712, 187812, 187912, 188012], [188112, 188212, 188312, 188412], [188512, 188612, 188712, 188812], [188912, 189012, 189112, 189212], [189312, 189412, 189512, 189612], [189712, 189812, 189912, 190012], [190112, 190212, 190312, 190412, 190512, 190612, 190712, 190812], [190912, 191012, 191112, 191212], [191312, 191412, 191512, 191612, 191712, 191812, 191912, 192012], [192112, 192212], [192312, 192412, 192512, 192612, 192712, 192812], [192912, 193012, 193112, 193212], [193401, 193501, 193601, 193701, 193801, 193901, 194001, 194101, 194201, 194301, 194401, 194501], [194601, 194701, 194801, 194901, 195001, 195101, 195201, 195301], [195302, 195401, 195501, 195601, 195701, 195801, 195901, 196001, 196101], [196101, 196201, 196301], [196401, 196501, 196601, 196701, 196801, 196901], [197001, 197101, 197201, 197302, 197401], [197501, 197601, 197701], [197801, 197901, 198001, 198101], [198201, 198301, 198401, 198502, 198602, 198701, 198801], [198902, 199001, 199101, 199201], [199302, 199401, 199501, 199601, 199702, 199801, 199901, 200001], [200102, 200109, 200201, 200301, 200401, 200502, 200601, 200701, 200801], [200902, 201001, 201101, 201201, 201302, 201401, 201501, 201601]];
      for (var i = 0; i < presidents.length; i++) {
        for (var j = 0; j < terms[i].length; j++) {
          fire.database().ref('presidents/' + presidents[i]).push(terms[i][j])
        }
      }
    }
    return (
      <button onClick={addPresidents}>
      Add to Firebase
      </button>
    )
  }

  render() {
    return (
      <div>
        {this.main()}
      </div>
    );
  }
}

export default App;
