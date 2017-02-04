package com.example.bharath.publicg;

import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;


public class MainPage extends AppCompatActivity {

    static final int REQUEST_IMAGE_CAPTURE = 1;
    ImageView image_view;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_page);
        Button cam_but = (Button) findViewById(R.id.cam_but);
        image_view = (ImageView)findViewById(R.id.image_viewID);
        if(!hasCamera())
            cam_but.setEnabled(false);
    }
    private boolean hasCamera(){
        return getPackageManager().hasSystemFeature(PackageManager.FEATURE_CAMERA_ANY);
    }
    public void launchCamera(View view){
        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(intent,REQUEST_IMAGE_CAPTURE);

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
       if(requestCode==REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK){
           Bundle extras  = data.getExtras();
           Bitmap photo = (Bitmap) extras.get("data");
           image_view.setImageBitmap(photo);
       }
    }
}

