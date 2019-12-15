<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');

    include_once('../config/Database.php');
    include_once('../models/Post.php');

    $database = new Database();
    $db = $database->connect();

    $post = new Post($db);
    $result = $post->all();

    if ($result->rowCount() > 0) {
        $response = array();
        $response['status'] = '1';
        $response['message'] = 'Showing all posts available at this time.';
        $response['data'] = array();

        while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
            array_push($response['data'], $row);
        }

        echo json_encode($response);

    } else {
        echo json_encode(
            array(
                'status' => '1',
                'message' => 'No posts available at this time.'
            )
        );

    }
?>
