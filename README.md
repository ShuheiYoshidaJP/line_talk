LINE TALK
LINEのトーク履歴を読み込むプロジェクト

line.py
このファイルは、textという文字列を受け取り、そのテキスト行のタイプ（date, time, または other）を識別し、コンテンツを取得する Line クラスを定義しています。

line_type.py
ここでは、 line.py で使用される LineType 列挙型を定義しています。これにより、読みやすさと信頼性を高めることができます。

message.py
このファイルには、日付、時間、送信者名、メッセージ本文などの情報を含む Message クラスが定義されています

data_file.py
最終的に、 DataFile クラスによって、特定のファイルパスからの情報を引数に、計算を実行し、処理されたメッセージのリスト（[Message1, Message2, ...]）を返すようになります。読み込まれた各 Line テキスト行に対して、 LineType を確認し、datetime、user、およびcontentの属性が設定された Message オブジェクトとして出力されます。