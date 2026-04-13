import { createContext, useEffect, useState } from "react";
import { api } from "./util";

export const Context = createContext();

export default function ContextProvider({ children }) {
  const [loading, setLoading] = useState(false);
  const [posts, setPosts] = useState([]);
  const [subs, setSubs] = useState([]);
  const [selectedSub, setSelectedSub] = useState(null);

  const getPosts = () => {
    setLoading(true);
    api("get_posts", { subName: selectedSub }, (data) => {
      setPosts(data.posts);
      setLoading(false);
    });
  };

  const getSubs = () => {
    setLoading(true);
    api("get_subs", {}, (data) => {
      setSubs(data.subs);
      setLoading(false);
    });
  };

  useEffect(() => {
    getSubs();
  }, []);

  useEffect(() => {
    getPosts();
  }, [selectedSub]);

  const contextValue = {
    loading: loading,
    setLoading: setLoading,
    posts: posts,
    setPosts: setPosts,
    getPosts: getPosts,
    subs: subs,
    setSubs: setSubs,
    selectedSub: selectedSub,
    setSelectedSub: setSelectedSub,
  };

  return <Context.Provider value={contextValue}>{children}</Context.Provider>;
}
