function csvToJson(){

  var file = document.querySelector('#getfile');
  // input 変化時に読み込む
  file.onchange = function(){
    var fileList = file.files;
    var reader = new FileReader();
    reader.readAsText(fileList[0]);
    //読み込み後表示
    reader.onload = function(){  

      // 配列を定義
      let csvArray = [];
      // 改行ごとに配列化
      let lines = reader.result.split(/\r\n|\n/);
      // 1行ごとに処理
      for (let i = 0; i < lines.length; ++i) {
          let cells = lines[i].split(",");
          if (cells.length != 1) {
              csvArray.push(cells);
          }
      }

      // コンソールに配列を出力
      console.log("------csvデータを配列に変換した文字列------");
      console.log(csvArray);

      //csvデータをjsonに変換
      var json_text = JSON.stringify(csvArray, null, " ");
      console.log("------csvデータを配列に変換し、Jsonに変換した文字列------");

      //コンソールにjsonデータを出力
      console.log(json_text);

      document.querySelector('#preview').textContent = json_text;
    };
  };
};

var form = document.getElementById("myform");

function test(){
  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());

  console.log(data); // {name: 'test', email: 'test@example.com', content: 'xxx'}

  try {
      // APIコール
      window.fetch("/", {
          method: "POST",
          body: JSON.stringify(data),
      });

      window.alert("送信しました。");

      // 完了時に入力値をクリア
      form.reset();

  } catch (e) {
      console.log(e);
  }
};