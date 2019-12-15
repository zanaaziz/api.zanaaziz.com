<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');

    include_once('../config/Database.php');
    include_once('../models/Post.php');

    $database = new Database();
    $db = $database->connect();

    $post = new Post($db);
    $result = $post->single(isset($_GET['id']) ? $_GET['id'] : die());

    if ($result->rowCount() > 0) {
        $response = array();
        $response['status'] = '1';
        $response['message'] = 'Showing the requested post.';
        $response['data'] = $result->fetch(PDO::FETCH_ASSOC);

        echo json_encode($response);

    } else {
        echo json_encode(
            array(
                'status' => '1',
                'message' => 'Could not find the requested post.'
            )
        );

    }
    
?>
