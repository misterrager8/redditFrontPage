import moment from "moment";

export default function PostItem({ item }) {
  return (
    <a className="between text-truncate" href={item.url} target="_blank">
      <div className="text-truncate">
        <div className="me-3">{item.score}</div>
        <div className="text-truncate">{item.title}</div>
      </div>
      <div>
        <div>{moment.unix(item.created_utc).format("M-D-YY @ h:mm A")}</div>
        <div className="ms-3">{item.num_comments}</div>
      </div>
    </a>
  );
}
