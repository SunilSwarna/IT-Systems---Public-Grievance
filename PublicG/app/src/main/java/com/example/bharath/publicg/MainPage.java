package com.example.bharath.publicg;

import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;


public class MainPage extends AppCompatActivity {

    static final int REQUEST_IMAGE_CAPTURE = 1;
    private static final String stringUrl = "https://public-grievence.000webhostapp.com/miracle.php";
    ImageView image_view;
    ImageButton galaryBut;
    ImageButton uploadBut;
    private String encoded_string;
    Bitmap image;
    private Uri imageSelect;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_page);
        Button cam_but = (Button) findViewById(R.id.cam_but);
        galaryBut = (ImageButton) findViewById(R.id.galarybut);
        image_view = (ImageView) findViewById(R.id.image_viewID);
        uploadBut = (ImageButton)findViewById(R.id.uploadBut);

        if (!hasCamera())
            cam_but.setEnabled(false);
        galaryBut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
                //File pic_Dir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES);
                String picName = getPicName();
                // File imageFile = new File(pic_Dir, picName);

                //intent.putExtra(MediaStore.EXTRA_OUTPUT, pictureUri);
                startActivityForResult(intent, REQUEST_IMAGE_CAPTURE);
            }
        });
        uploadBut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                image = ((BitmapDrawable) image_view.getDrawable()).getBitmap();
                new UploadImage().execute();
                Toast.makeText(MainPage.this, "Image Uploaded",
                        Toast.LENGTH_LONG).show();
            }
        });

    }

    private boolean hasCamera() {
        return getPackageManager().hasSystemFeature(PackageManager.FEATURE_CAMERA_ANY);
    }

   /* public void launchCamera(View view) {
        switch (view.getId()) {
            case R.id.galarybut:
                Intent intent = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
                //File pic_Dir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES);
                String picName = getPicName();
                // File imageFile = new File(pic_Dir, picName);

                //intent.putExtra(MediaStore.EXTRA_OUTPUT, pictureUri);
                startActivityForResult(intent, REQUEST_IMAGE_CAPTURE);
                break;
            case R.id.uploadBut:
                image = ((BitmapDrawable) image_view.getDrawable()).getBitmap();
                new UploadImage().execute();
                break;
        }
    }*/
    private String getPicName() {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd_HHmmss");
        String timeStamp = sdf.format(new Date());
        return "publicG" + timeStamp + ".jpg";

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK && data != null) {
            imageSelect = data.getData();
            InputStream inputStream;
           /* try {
                inputStream = getContentResolver().openInputStream(imageSelect);
                Bitmap image = BitmapFactory.decodeStream(inputStream);
               // ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
               // image.compress(Bitmap.CompressFormat.JPEG, 100,byteStream);
                //image.recycle();

                //byte[] array = byteStream.toByteArray();
                //String encoded_string = Base64.encodeToString(array, 0);
                System.out.println("SEE OUT PUT HERE======= "+encoded_string);
            }catch (FileNotFoundException e) {
                e.printStackTrace();
            }*/
            image_view.setImageURI(imageSelect);
        }
    }
    private class UploadImage extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... params) {
            ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
            image.compress(Bitmap.CompressFormat.JPEG, 100, byteStream);
            //image.recycle();
            byte[] array = byteStream.toByteArray();
            encoded_string = Base64.encodeToString(array, 0);
            return null;
            //String encoded_string = Base64.encodeToString(byteStream.toByteArray(), Base64.DEFAULT);
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            makeRequest();
        }
    }
    private void makeRequest() {
        RequestQueue requestQueue = Volley.newRequestQueue(this);
        StringRequest request = new StringRequest(Request.Method.POST, "http://130.211.224.94/miracle.php",
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

            }
        }) {
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                HashMap<String,String> map = new HashMap<>();
                map.put("encoded_string",encoded_string);
                return map;
            }
        };
        requestQueue.add(request);
    }
}

