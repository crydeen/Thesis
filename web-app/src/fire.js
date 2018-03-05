import firebase from 'firebase'
var config = {
    apiKey: "AIzaSyBEp4tZYAQPqZpETn--YekFgn8YlUS0BOc",
    authDomain: "thesis-dcrydeen.firebaseapp.com",
    databaseURL: "https://thesis-dcrydeen.firebaseio.com",
    projectId: "thesis-dcrydeen",
    storageBucket: "thesis-dcrydeen.appspot.com",
    messagingSenderId: "355939498361"
  };
var fire = firebase.initializeApp(config);
export default fire;
