<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: POST,OPTIONS');
    header('Access-Control-Allow-Headers: Content-Type,Authorization,X-Requested-With');

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

    if (!$api->verify($data->token)) {
        echo json_encode(
            array(
                'message' => 'You are not authorized to use this API.'
            )
        );

        die();
    }

    if ($api->delete($data->id)) {
        echo json_encode(
            array(
                'message' => 'The requested post has been deleted.'
            )
        );
        
    } else {
        echo json_encode(
            array(
                'message' => 'Something went wrong, the requested post has not been deleted.'
            )
        );

    }
    
?>
