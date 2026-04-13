import { useContext } from "react";
import { Context } from "./context";
import PostItem from "./components/items/PostItem";
import SubItem from "./components/items/SubItem";

export default function Display() {
  const ctx = useContext(Context);

  return (
    <div className="p-4">
      <div className="d-flex">
        <div className="subs-scroll">
          <div className={"mb-3 " + (ctx.loading ? "" : "invisible")}>
            <span className="spinner-border spinner-border-sm my-auto mx-2"></span>
          </div>
          {ctx.subs.map((x) => (
            <SubItem item={x} />
          ))}
        </div>

        <div className="posts-scroll">
          {ctx.posts.map((x) => (
            <PostItem item={x} />
          ))}
        </div>
      </div>
    </div>
  );
}
