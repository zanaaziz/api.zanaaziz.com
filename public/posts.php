<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: GET');

    include_once('../private/database.php');
    include_once('../private/api.php');

    $database = new Database();
    $db = $database->connect();

    $api = new API($db);
    $result = $api->read_all();

    if ($result->rowCount() > 0) {
        $response = array();
        $response['message'] = 'Showing all posts available at this time.';
        $response['data'] = array();

        while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
            array_push($response['data'], $row);
        }

        echo json_encode($response);

    } else {
        echo json_encode(
            array(
                'message' => 'No posts available at this time.'
            )
        );

    }
?>
