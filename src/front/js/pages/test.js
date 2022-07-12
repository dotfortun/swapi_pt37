import React from "react";
import { useParams } from "react-router-dom";

const ConditionalComp = () => {
  const { pageType } = useParams();

  switch (pageType) {
    case "planet":
      return <div>This is a planet</div>;
      break;

    case "person":
      return <div>This is a person</div>;
      break;

    case "vehicle":
      return <div>This is a vehicle</div>;
      break;

    default:
      return <div>Something went wrong.</div>;
      break;
  }
};

export { ConditionalComp };
