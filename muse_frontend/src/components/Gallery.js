import React, { useState, useEffect } from "react";
import axios from "./axios";
import "./Gallery.css";

function GalleryImages({ match }) {
  const [images, setImages] = useState(null);
  const [addImage, setAddImage] = useState(null);
  const [updateImages, setUpdateImages] = useState(0);

  useEffect(() => {
    async function fetchImages() {
      const res = await axios.get(`localhost:8000/gallery/${match.id}`);
      console.log(res);
      setImages(res.data.images);
      return res;
    }
    window.scrollTo(0, 0);

    fetchImages();
  }, [updateFilms]);

  return (
    <div>
      <>
        {films && (
          <>
            <Button
              variant="outline-light"
              className="addImageButton"
              onClick={() => setAddImage(true)}
            >
              Add Image
            </Button>
            <div className="galleryContainer">
              {images.length > 0 && (
                <>
                  {films.map((id) => (
                    <div className="imageContainer">
                      <img></img>
                    </div>
                  ))}
                </>
              )}
            </div>
          </>
        )}
      </>
    </div>
  );
}
