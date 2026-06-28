<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <?php
    // URL引数 "p" を取得。なければデフォルト値を設定
    $colors = isset($_GET['p']) ? $_GET['p'] : 'NjZK8u7m-.6mn.sSN.fGae7B_nb7q1Mj08Mbw-w8PD';
    
    // CGIのURLを組み立て
    $cgi_url = "https://kurajo.ivory.ne.jp/rakugaki_pao/palette/image.cgi?colors=" . htmlspecialchars($colors);
    ?>
    <meta property="og:image" content="<?php echo $cgi_url; ?>">
    <meta property="og:title" content="rakugaki_pao - Custom Palette">
    
    <meta name="twitter:card" content="summary">
    <meta name="twitter:image" content="<?php echo $cgi_url; ?>">
    <meta name="twitter:title" content="rakugaki_pao - Custom Palette">

    <link rel="icon" href="image/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="image/apple-touch-icon.png">
    <title>rakugaki_pao</title>
    <link rel="stylesheet" type="text/css" href="style.css?v=1">
</head>
<body>
    <script>
        window.location.href = `palette/index.html${window.location.search}`;   
    </script>
</body>