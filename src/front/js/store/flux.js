const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      message: null,
      demo: [
        {
          title: "FIRST",
          background: "white",
          initial: "white",
        },
        {
          title: "SECOND",
          background: "white",
          initial: "white",
        },
      ],
      books: [
        {
          title: "Neuromancer",
          author: "William Gibson",
          year_published: 1984,
          isbn: "",
          rating: 90,
          is_checked_out: false,
        },
        {
          title: "Snow Crash",
          author: "Neal Stephenson",
          year_published: 1992,
          isbn: "978-01336162-0",
          rating: 95,
          is_checked_out: true,
        },
        {
          title: "Altered Carbon",
          author: "Richard K. Morgan",
          year_published: 2002,
          isbn: "",
          rating: 100,
          is_checked_out: false,
        },
        {
          title: "Cryptonomicon",
          author: "Neal Stephenson",
          year_published: 1999,
          isbn: "978-0-380-78862-0",
          rating: 85,
          is_checked_out: false,
        },
      ],
    },
    actions: {
      // Use getActions to call a function within a fuction
      exampleFunction: () => {
        getActions().changeColor(0, "green");
      },

      getMessage: async () => {
        try {
          // fetching data from the backend
          const resp = await fetch(process.env.BACKEND_URL + "/api/hello");
          const data = await resp.json();
          setStore({ message: data.message });
          // don't forget to return something, that is how the async resolves
          return data;
        } catch (error) {
          console.log("Error loading message from backend", error);
        }
      },
      changeColor: (index, color) => {
        //get the store
        const store = getStore();

        //we have to loop the entire demo array to look for the respective index
        //and change its color
        const demo = store.demo.map((elm, i) => {
          if (i === index) elm.background = color;
          return elm;
        });

        //reset the global store
        setStore({ demo: demo });
      },
    },
  };
};

export default getState;
