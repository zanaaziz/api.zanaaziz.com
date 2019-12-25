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

    if ($api->login($data->username, $data->password)) {
        echo json_encode(
            array(
                'authentication' => '1',
                'message' => 'User authentication succeeded.'
            )
        );
        
    } else {
        echo json_encode(
            array(
                'authentication' => '0',
                'message' => 'User authentication failed.'
            )
        );

    }
    
?>
