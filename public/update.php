<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: PUT,OPTIONS');
    header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Access-Control-Allow-Methods,Content-Type,Authorization,X-Requested-With');

    if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
        header('HTTP/1.1 200 OK');
        return;
    }

    include_once('../private/database.php');
    include_once('../private/api.php');

    $database = new Database();
    $db = $database->connect();

    $api = new API($db);
    
    $data = json_decode(file_get_contents('php://input'));

    if ($api->update($data->id, $data->title, $data->image, $data->body)) {
        echo json_encode(
            array(
                'message' => 'The requested post has been updated.'
            )
        );
        
    } else {
        echo json_encode(
            array(
                'message' => 'Something went wrong, the requested post has not been updated.'
            )
        );

    }
    
?>
