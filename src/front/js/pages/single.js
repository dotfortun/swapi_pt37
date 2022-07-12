import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";

export const Single = (props) => {
  const { store, actions } = useContext(Context);
  const { id } = useParams();

  return (
    <div className="jumbotron">
      <h1 className="display-4">
        This is the value of id: {id}
      </h1>
      <hr className="my-4" />
      <ul>
        <li>{store.books[id]?.title}</li>
        <li>{store.books[id]?.author}</li>
        <li>{store.books[id]?.year_published}</li>
        <li>{store.books[id]?.isbn}</li>
        <li>{store.books[id]?.rating}</li>
      </ul>

      <Link to="/">
        <span className="btn btn-primary btn-lg" href="#" role="button">
          Back home
        </span>
      </Link>
    </div>
  );
};

Single.propTypes = {
  match: PropTypes.object,
};
