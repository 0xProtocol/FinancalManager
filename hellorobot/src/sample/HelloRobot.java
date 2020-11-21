package sample;

import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Bounds;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseButton;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;
import javafx.util.Duration;

public class HelloRobot extends Application {

    private static final int BOARD_SIZE = 600;
    @Override
    public void start(Stage primaryStage) throws Exception{
        Group robot = FXMLLoader.load(getClass().getResource("robot.fxml"));
        robot.setLayoutX(150);
        robot.setLayoutY(100);
        Group root = new Group();
        Button revive = new Button();
        revive.setText("Revive");
        revive.setPrefSize(100,30);
        revive.setLayoutX(5);
        revive.setLayoutY(5);
        revive.setOnAction(e -> {
            Label label = (Label) robot.lookup("#label");
            if(robot.isVisible()){
                label.setText("!Dead yet!?");
            } else {
                robot.setVisible(true);
                label.setText("Be nice this time!");
            }
        });
        root.getChildren().addAll(robot, revive);
        Scene scene = new Scene(root, BOARD_SIZE, BOARD_SIZE);
        scene.addEventHandler(KeyEvent.KEY_PRESSED, e -> {
            if(e.getCode().equals(KeyCode.Q)){
                Platform.exit();
                System.exit(0);
            }
        });

        scene.addEventHandler(MouseEvent.MOUSE_CLICKED, e -> {
            if(e.getButton() == MouseButton.SECONDARY) {
                Bounds b = robot.getLayoutBounds();
                Timeline animation = new Timeline(
                        new KeyFrame(
                                Duration.millis(700),
                                new KeyValue(robot.layoutXProperty(), e.getX() - b.getWidth()/2),
                                new KeyValue(robot.layoutYProperty(), e.getY() - b.getHeight()/2))
                );
                animation.play();
            }
        });

        //root.getChildren().add(createRobot());
        robot.addEventHandler(MouseEvent.ANY, new DragEventHandler(robot));
        primaryStage.setTitle("Hello Robot");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
