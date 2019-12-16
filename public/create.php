<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: POST');
    header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Access-Control-Allow-Methods,Content-Type,Authorization,X-Requested-With');

    include_once('../private/database.php');
    include_once('../private/api.php');

    $database = new Database();
    $db = $database->connect();

    $api = new API($db);
    
    $data = json_decode(file_get_contents('php://input'));

    if ($api->create($data->title, $data->image, $data->body)) {
        echo json_encode(
            array(
                'message' => 'A new post has been created.'
            )
        );
        
    } else {
        echo json_encode(
            array(
                'message' => 'Something went wrong, a new post has not been created.'
            )
        );

    }
    
?>
