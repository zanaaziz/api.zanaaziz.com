<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: DELETE');
    header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Access-Control-Allow-Methods,Content-Type,Authorization,X-Requested-With');

    include_once('../private/database.php');
    include_once('../private/api.php');

    $database = new Database();
    $db = $database->connect();

    $api = new API($db);
    
    $data = json_decode(file_get_contents('php://input'));

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
